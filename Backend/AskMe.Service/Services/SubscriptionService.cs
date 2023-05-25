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

    public async Task<SubscriptionResponse[]> SubscriptionsWithoutChildrenAsync(string userLogin)
    {
        var authorSubscriptions = await GetAuthorSubscriptionsAsync(userLogin);
        var subsWithoutChildren = authorSubscriptions
            .Where(x => authorSubscriptions.All(children => children.ParentSubscriptionId != x.Id))
            .ToArray();

        return subsWithoutChildren;
    }

    public async Task SubscribeAsync(Guid subscriptionId)
    {
        var currentUser = await userService.ReadUserByLoginAsync(userIdentity.CurrentUser!.Login);
        var boughtSubscription = new BoughtSubscription
        {
            Id = Guid.NewGuid(),
            OwnerId = currentUser.Id,
            SubscriptionId = subscriptionId
        };

        await dbContext.BoughtSubscriptions.AddAsync(boughtSubscription);
        await dbContext.SaveChangesAsync();
    }

    public async Task UnsubscribeAsync(Guid subscriptionId)
    {
        var currentUser = await userService.ReadUserByLoginAsync(userIdentity.CurrentUser!.Login);

        var boughtSubscription = await dbContext.BoughtSubscriptions
            .FirstOrDefaultAsync(x => x.SubscriptionId == subscriptionId && x.OwnerId == currentUser.Id);
        if (boughtSubscription == null)
        {
            throw new ArgumentNullException($"У пользователя {currentUser.Login} нет подписки {subscriptionId}");
        }

        dbContext.BoughtSubscriptions.Remove(boughtSubscription);
        await dbContext.SaveChangesAsync();
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
