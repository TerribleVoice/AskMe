using AskMe.Core.Models;

namespace AskMe.Core.StorageLayer.Repositories;

public interface IUserSubscriptionRepository
{
    Task<Guid[]> SelectSubscriptionIdsByUserId(Guid id);
    Task<Result> Create(Guid userId, Guid subscriptionId);
    Task<Result> Delete(Guid userId, Guid subscriptionId);
}
