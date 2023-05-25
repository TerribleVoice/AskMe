using AskMe.Core.Models;
using AskMe.Core.Models.Dbo;
using AskMe.Core.StorageLayer;
using AskMe.Service.Converters;
using AskMe.Service.Models;
using Microsoft.EntityFrameworkCore;

namespace AskMe.Service.Services;

public class SubscriptionService : ISubscriptionService
{
    private readonly ISubscriptionConverter subscriptionConverter;
    private readonly IUserIdentity userIdentity;
    private readonly IUserService userService;
    private readonly PostgresDbContext dbContext;

    public SubscriptionService(ISubscriptionConverter subscriptionConverter,
        IUserIdentity userIdentity,
        IUserService userService,
        PostgresDbContext dbContext
    )
    {
        this.subscriptionConverter = subscriptionConverter;
        this.userIdentity = userIdentity;
        this.userService = userService;
        this.dbContext = dbContext;
    }

    public async Task CreateOrUpdateAsync(SubscriptionRequest request, Guid? subscriptionId = null)
    {
        var id = subscriptionId ?? Guid.NewGuid();
        var authorId = userIdentity.CurrentUser!.Id;
        var subscriptionDbo = subscriptionConverter.Convert(id, authorId, request);

        if (subscriptionId.HasValue)
        {
            dbContext.Subscription.Update(subscriptionDbo);
        }
        else
        {
            await dbContext.Subscription.AddAsync(subscriptionDbo);
        }
        await dbContext.SaveChangesAsync();
    }

    public async Task DeleteAsync(Guid id)
    {
        await ThrowIfCantBeEditedAsync(id);

        var subscription = await dbContext.ReadAsync<Subscription>(id);
        dbContext.Subscription.Remove(subscription);
    }

    public async Task<SubscriptionResponse[]> GetAuthorSubscriptionsAsync(string userLogin)
    {
        var subscriptions = await dbContext.Subscription
            .Where(x=>x.Author.Login == userLogin)
            .ToArrayAsync();

        return subscriptions.Select(subscriptionConverter.Convert).ToArray();
    }

    public async Task<SubscriptionResponse[]> GetReaderSubscriptionsAsync(string userLogin)
    {
        var subscriptions = await dbContext.BoughtSubscriptions
            .Where(x => x.Owner.Login == userLogin)
            .Select(x => x.Subscription)
            .ToArrayAsync();

        return subscriptions.Select(subscriptionConverter.Convert).ToArray();
    }

    public async Task<SubscriptionResponse[]> GetReaderSubscriptionsFlatTreeAsync(string userLogin)
    {
        var boughtSubscriptions = await GetReaderSubscriptionsAsync(userLogin);
        var parentSubscriptionsFlatTreeQuery =
            GetParentSubscriptionsRecursive(boughtSubscriptions.Select(x => subscriptionConverter.Convert(x)));
        var parentSubscriptionsFlatTree = parentSubscriptionsFlatTreeQuery == null
            ? Array.Empty<SubscriptionResponse>()
            : (await parentSubscriptionsFlatTreeQuery.ToArrayAsync()).Select(subscriptionConverter.Convert).ToArray();

        return boughtSubscriptions.UnionBy(parentSubscriptionsFlatTree, x => x.Id).ToArray();

        IQueryable<Subscription>? GetParentSubscriptionsRecursive(
            IEnumerable<Subscription> childSubscriptions,
            IQueryable<Subscription>? query = null)
        {
            var parentIds = childSubscriptions.Where(x => x.ParentSubscriptionId.HasValue)
                .Select(x => x.ParentSubscriptionId).ToArray();
            if (parentIds.Length > 0)
            {
                var ids = parentIds;
                var subscriptionQuery = dbContext.Subscription.Where(x => ids.Contains(x.Id));
                query = query?.UnionBy(subscriptionQuery, x => x.Id) ?? subscriptionQuery;
                GetParentSubscriptionsRecursive(subscriptionQuery, query);
            }
            return query;
        }
    }

    public async Task<Result> SubscribeAsync(Guid subscriptionId)
    {
        throw new NotImplementedException("Нужно разобраться с тем как оплачивать");
    }

    public async Task<Result> UnsubscribeAsync(Guid subscriptionId)
    {
        throw new NotImplementedException("Нужно подумать с циклом оплаты подписки");
    }

    private async Task ThrowIfCantBeEditedAsync(Guid subscriptionId)
    {
        var subscription = await dbContext.ReadAsync<Subscription>(subscriptionId);;

        if (subscription.AuthorId != userIdentity.CurrentUser!.Id)
        {
            throw new Exception($"Подписка {subscriptionId} не может быть редактирована пользователем {userIdentity.CurrentUser.Login}");
        }
    }
}
