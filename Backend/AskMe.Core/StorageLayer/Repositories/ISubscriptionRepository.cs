using AskMe.Core.Models;
using AskMe.Core.Models.Dbo;

namespace AskMe.Core.StorageLayer.Repositories;

public interface ISubscriptionRepository
{
    Task<Subscription[]> SelectByAuthorId(Guid authorId);
    Task<Subscription[]> SelectByIds(Guid[] ids);
    Task<Subscription?> Find(Guid id);
    Task<Result<Subscription>> Read(Guid id);
    Task<Result> Create(Subscription subscription);
    Task<Result> Update(Subscription subscription);
    Task<Result> Delete(Guid id);
}
