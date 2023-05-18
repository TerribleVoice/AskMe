using AskMe.Core.Models;
using AskMe.Service.Models;

namespace AskMe.Service.Services;

public interface IFeedService
{
    Task<PostResponse[]> GetFeedAsync(string userLogin, DateTime? timeAfter = null);
    Task CreateOrUpdateAsync(PostRequest request, Guid? postId = null);
    Task DeleteAsync(Guid postId);
    Result Buy(Guid postId);
    Task<Dictionary<Guid, bool>> IsUserHaveAccessToPostsAsync(string userLogin, PostResponse[] postId);
    Task<PostResponse> ReadAsync(Guid postId);
    Task<PostResponse[]> GetUserPostsAsync(string userLogin);
}
