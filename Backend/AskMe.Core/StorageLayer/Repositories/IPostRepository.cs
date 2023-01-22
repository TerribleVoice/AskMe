using AskMe.Core.Models;
using AskMe.Core.Models.Dbo;

namespace AskMe.Core.StorageLayer.Repositories;

public interface IPostRepository
{
    Task<Post[]> Select(Guid authorId, DateTime? timeFilter = null);
    Task<Post?> Find(Guid id);
    Task<Result<Post>> Read(Guid id);
    Task<Result> Create(Post post);
    Task<Result> Update(Post post);
    Task<Result> Delete(Guid id);
}
