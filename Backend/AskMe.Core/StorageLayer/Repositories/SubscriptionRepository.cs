using AskMe.Core.Models;
using AskMe.Core.Models.Dbo;
using Microsoft.EntityFrameworkCore;

namespace AskMe.Core.StorageLayer.Repositories;

public class SubscriptionRepository : ISubscriptionRepository
{
    private readonly PostgresDbContext postgresDbContext;

    public SubscriptionRepository(PostgresDbContext postgresDbContext)
    {
        this.postgresDbContext = postgresDbContext;
    }

    public Task<Subscription[]> SelectByAuthorId(Guid authorId)
    {
        return postgresDbContext.Subscription.Where(x => x.AuthorId == authorId).ToArrayAsync();
    }

    public Task<Subscription[]> SelectByIds(Guid[] ids)
    {
        return postgresDbContext.Subscription.Where(x=>ids.Contains(x.Id)).ToArrayAsync();
    }

    public Task<Subscription?> Find(Guid id)
    {
        return postgresDbContext.Subscription.FirstOrDefaultAsync(x => x.Id == id);
    }

    public async Task<Result<Subscription>> Read(Guid id)
    {
        var post = await Find(id);
        return post != null
            ? Result.Ok(post)
            : Result.Fail<Subscription>("Подписка с таким id не существует");
    }

    public async Task<Result> Create(Subscription subscription)
    {
        var postWithSameId = await Find(subscription.Id);
        if (postWithSameId != null)
        {
            return Result.Fail("Подписка с таким id уже существует");
        }
        await postgresDbContext.Subscription.AddAsync(subscription);
        await postgresDbContext.SaveChangesAsync();
        return Result.Ok();
    }

    public async Task<Result> Update(Subscription subscription)
    {
        var readResult = await Read(subscription.Id);
        if (readResult.IsFailure)
        {
            return readResult;
        }

        var existed = readResult.Value!;
        existed.Description = subscription.Description;
        existed.Name = subscription.Name;
        existed.Price = subscription.Price;
        existed.ParentSubscriptionId = subscription.ParentSubscriptionId;

        postgresDbContext.Subscription.Update(existed);
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

        postgresDbContext.Subscription.Remove(readResult.Value!);
        await postgresDbContext.SaveChangesAsync();
        return Result.Ok();
    }
}
