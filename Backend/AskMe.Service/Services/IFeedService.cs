using AskMe.Service.Models;
using AskMe.WebApi.Models;

namespace AskMe.Service.Services;

public interface IFeedService
{
    Task<PostResponse[]> GetFeedAsync(string userLogin, int skip = 0, int take = 10);
    Task<PostResponse[]> GetUserPostsAsync(string userLogin, int skip = 0, int take = 10);
    Task<Guid> CreateOrUpdateAsync(PostRequest request, Guid? postId = null);
    Task DeleteAsync(Guid postId);
    Task<Dictionary<Guid, bool>> IsUserHaveAccessToPostsAsync(string userLogin, PostResponse[] postId);
    Task<PostResponse> ReadAsync(Guid postId);
    Task AttachFilesAsync(Guid postId, AttachmentRequest[] fileStreamWithNames);
    Task<AttachmentResponse[]> GetPostAttachmentUrlsAsync(Guid postId);
}
