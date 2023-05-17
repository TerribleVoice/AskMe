using AskMe.Core.Models;
using AskMe.Core.Models.Dbo;
using AskMe.Core.StorageLayer;
using AskMe.Service.Converters;
using AskMe.Service.Models;
using Microsoft.EntityFrameworkCore;

namespace AskMe.Service.Services;

public class FeedService : IFeedService
{
    private readonly PostgresDbContext dbContext;
    private readonly IUserService userService;
    private readonly IPostConverter postConverter;
    private readonly IUserIdentity userIdentity;

    public FeedService(
        PostgresDbContext dbContext,
        IUserService userService,
        IPostConverter postConverter,
        IUserIdentity userIdentity
        )
    {
        this.dbContext = dbContext;
        this.userService = userService;
        this.postConverter = postConverter;
        this.userIdentity = userIdentity;
    }

    public async Task<PostResponse[]> SelectAsync(string userLogin, DateTime? timeAfter = null)
    {
        var user = await userService.FindUserByLoginAsync(userLogin);

        var posts = await dbContext.Posts.Where(x => x.AuthorId == user.Id).FilterByTime(timeAfter).ToArrayAsync();
        return posts.Select(postConverter.Convert).ToArray();
    }

    public async Task<PostResponse> ReadAsync(Guid postId)
    {
        var post = await dbContext.ReadAsync<Post>(postId);

        return postConverter.Convert(post);
    }

    public async Task CreateOrUpdateAsync(PostRequest request, Guid? postId = null)
    {
        if (postId.HasValue)
        {
            await ThrowIfCantEdit(postId.Value);
        }

        var id = postId ?? Guid.NewGuid();
        var authorId = userIdentity.CurrentUser!.Id;
        var postDbo = postConverter.Convert(id, authorId, DateTime.Now, request);
        postDbo.TimeToUtc();

        if (postId.HasValue)
        {
            dbContext.Posts.Update(postDbo);
        }
        else
        {
            dbContext.Posts.Add(postDbo);
        }

        await dbContext.SaveChangesAsync();
    }

    public async Task DeleteAsync(Guid postId)
    {
        await ThrowIfCantEdit(postId);

        var post = await dbContext.ReadAsync<Post>(postId);
        dbContext.Posts.Remove(post);
        await dbContext.SaveChangesAsync();
    }

    public async Task<Dictionary<Guid, bool>> IsUserHaveAccessToPostAsync(string userLogin, Guid[] postIds)
    {
        throw new NotImplementedException();
    }

    public Result Buy(Guid postId)
    {
        throw new NotImplementedException();
    }

    private async Task ThrowIfCantEdit(Guid postId)
    {
        var readResult = await dbContext.Posts.FirstAsync(x => x.Id == postId);

        if (readResult.AuthorId != userIdentity.CurrentUser!.Id)
        {
            throw new Exception("Авторизованный пользователь не является автором поста. Он не имет прав на действия с постом");
        }
    }
}
