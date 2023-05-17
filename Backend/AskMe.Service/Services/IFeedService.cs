using AskMe.Core.Models;
using AskMe.Service.Models;

namespace AskMe.Service.Services;

public interface IFeedService
{
    Task<PostResponse[]> SelectAsync(string userLogin, DateTime? timeAfter = null);
    Task CreateOrUpdateAsync(PostRequest request, Guid? postId = null);
    Task DeleteAsync(Guid postId);
    Result Buy(Guid postId);
    Task<Dictionary<Guid, bool>> IsUserHaveAccessToPostAsync(string userLogin, Guid[] postIds);
    Task<PostResponse> ReadAsync(Guid postId);
}
