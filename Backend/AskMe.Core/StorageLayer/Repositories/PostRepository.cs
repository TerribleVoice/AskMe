using AskMe.Core.Models;
using AskMe.Core.Models.Dbo;
using Microsoft.EntityFrameworkCore;

namespace AskMe.Core.StorageLayer.Repositories;

public class PostRepository : IPostRepository
{
    private readonly PostgresDbContext postgresDbContext;

    public PostRepository(PostgresDbContext postgresDbContext)
    {
        this.postgresDbContext = postgresDbContext;
    }

    public async Task<Post[]> SelectByAuthorId(Guid authorId, DateTime? timeFilter = null)
    {
        var posts = postgresDbContext.Posts.Where(x=>x.AuthorId == authorId);
        if (timeFilter.HasValue)
        {
            //todo добавить конвертацию часовых поясов
            var timeUtc = timeFilter.Value.ToUniversalTime();

            posts = posts.Where(x => x.CreatedAt >= timeUtc);
        }
        return await posts.ToArrayAsync();
    }

    public async Task<Result<Post>> Read(Guid id)
    {
        var post = await Find(id);
        return post != null
            ? Result.Ok(post)
            : Result.Fail<Post>("Пост с таким id не существует");
    }

    public async Task<Result> Create(Post post)
    {
        var postWithSameId = await Find(post.Id);
        if (postWithSameId != null)
        {
            return Result.Fail("Пост с таким id уже существует");
        }
        post.TimeToUtc();
        await postgresDbContext.Posts.AddAsync(post);
        await postgresDbContext.SaveChangesAsync();
        return Result.Ok();
    }

    public async Task<Post?> Find(Guid id)
    {
        return await postgresDbContext.Posts.FirstOrDefaultAsync(x => x.Id == id);
    }

    public async Task<Result> Update(Post post)
    {
        var readResult = await Read(post.Id);
        if (readResult.IsFailure)
        {
            return readResult;
        }

        var existedPost = readResult.Value!;
        existedPost.TimeToUtc();
        existedPost.Content = post.Content;
        existedPost.Price = post.Price;
        existedPost.SubscriptionId = post.SubscriptionId;

        postgresDbContext.Update(existedPost);
        await postgresDbContext.SaveChangesAsync();
        return Result.Ok();
    }

    public async Task<Result> Delete(Guid id)
    {
        var readResult = await Read(id);
        if (readResult.IsFailure)
        {
            return readResult;
        }

        postgresDbContext.Posts.Remove(readResult.Value!);
        await postgresDbContext.SaveChangesAsync();
        return Result.Ok();
    }
}
