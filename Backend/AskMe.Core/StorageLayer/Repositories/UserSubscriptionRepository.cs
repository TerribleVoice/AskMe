using AskMe.Core.Models;
using AskMe.Core.Models.Dbo;
using Microsoft.EntityFrameworkCore;

namespace AskMe.Core.StorageLayer.Repositories;

public class UserSubscriptionRepository : IUserSubscriptionRepository
{
    private readonly PostgresDbContext postgresDbContext;

    public UserSubscriptionRepository(PostgresDbContext postgresDbContext)
    {
        this.postgresDbContext = postgresDbContext;
    }
    public Task<Guid[]> SelectSubscriptionIdsByUserId(Guid id)
    {
        return postgresDbContext.UserSubscription.Where(x => x.UserId == id).Select(x=>x.UserId).ToArrayAsync();
    }

    public async Task<Result> Create(Guid userId, Guid subscriptionId)
    {
        var existed = await postgresDbContext.UserSubscription.FirstOrDefaultAsync(
            x => x.UserId == userId && x.SubscriptionId == subscriptionId);
        if (existed != null)
        {
            return Result.Fail($"Пользователь {userId} уже имеет подписку {subscriptionId}");
        }
        var dbo = new UserSubscription(userId, subscriptionId);
        postgresDbContext.UserSubscription.Add(dbo);
        await postgresDbContext.SaveChangesAsync();

        return Result.Ok();
    }

    public async Task<Result> Delete(Guid userId, Guid subscriptionId)
    {
        var existed = await postgresDbContext.UserSubscription.FirstOrDefaultAsync(
            x => x.UserId == userId && x.SubscriptionId == subscriptionId);
        if (existed == null)
        {
            return Result.Fail($"Пользователь {userId} не имеет подписки {subscriptionId}");
        }
        postgresDbContext.UserSubscription.Remove(existed);
        await postgresDbContext.SaveChangesAsync();

        return Result.Ok();
    }
}
