using AskMe.Core.Models;
using AskMe.Service.Models;

namespace AskMe.Service.Services;

public interface ISubscriptionService
{
    public Task CreateOrUpdateAsync(SubscriptionRequest request, Guid? subscriptionId = null);
    public Task DeleteAsync(Guid id);
    public Task<SubscriptionResponse[]> GetAuthorSubscriptionsAsync(string userLogin);
    public Task<SubscriptionResponse[]> GetReaderSubscriptionsAsync(string userLogin);
    public Task<Result> SubscribeAsync(Guid subscriptionId);
    public Task<Result> UnsubscribeAsync(Guid subscriptionId);


}
