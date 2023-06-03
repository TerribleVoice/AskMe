using AskMe.Core.Models;
using AskMe.Core.Models.Dbo;
using AskMe.Service.Services;
using AskMe.WebApi.Models;

namespace AskMe.WebApi.Builders;

public class SubscriptionViewModelBuilder
{
    private readonly ISubscriptionService subscriptionService;
    private readonly User? currentUser;


    public SubscriptionViewModelBuilder(IUserIdentity userIdentity,
        ISubscriptionService subscriptionService)
    {
        this.subscriptionService = subscriptionService;
        currentUser = userIdentity.CurrentUser;
    }

    public async Task<SubscriptionViewModel[]> BuildCreatedListAsync(string userLogin)
    {
        var authorSubscriptionsTask = subscriptionService.GetAuthorSubscriptionsAsync(userLogin);
        var currentUserSubscriptionIds = currentUser == null
            ? new HashSet<Guid>()
            : (await subscriptionService.GetReaderSubscriptionsAsync(currentUser.Login)).Select(x=>x.Id).ToHashSet();
        var currentUserInheritSubscriptionIds = currentUser == null
            ? new HashSet<Guid>()
            : (await subscriptionService.GetReaderSubscriptionsFlatTreeAsync(currentUser.Login))
            .Select(x => x.Id)
            .Except(currentUserSubscriptionIds)
            .ToHashSet();

        return (await authorSubscriptionsTask).Select(x => new SubscriptionViewModel
            {
                Name = x.Name,
                Description = x.Description,
                AuthorId = x.AuthorId,
                Price = x.Price,
                IsBought = currentUserSubscriptionIds.Contains(x.Id),
                IsInherit = currentUserInheritSubscriptionIds.Contains(x.Id)
            })
            .ToArray();
    }

    public async Task<SubscriptionViewModel[]> BuildBoughtListAsync(string userLogin)
    {
        var currentUserSubscriptionIds = await subscriptionService.GetReaderSubscriptionsAsync(userLogin);
        return currentUserSubscriptionIds.Select(x => new SubscriptionViewModel
            {
                Name = x.Name,
                Description = x.Description,
                AuthorId = x.AuthorId,
                Price = x.Price,
                IsBought = true,
                IsInherit = false
            })
            .ToArray();
    }
}
