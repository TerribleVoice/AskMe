using AskMe.Core.Models;
using AskMe.Service.Models;

namespace AskMe.Service.Services;

public interface ISubscriptionService
{
    public Task<Result> CreateOrUpdate(SubscriptionRequest request, Guid? subscriptionId = null);
    public Task<Result> Delete(Guid id);
    public Task<SubscriptionResponse[]> GetAuthorSubscriptions(string userLogin);
    public Task<SubscriptionResponse[]> GetReaderSubscriptions(string userLogin);
    public Task<Result> Subscribe(Guid userId, Guid subscriptionId);
    public Task<Result> Unsubscribe(Guid userId, Guid subscriptionId);


}
