using AskMe.Core.Models;
using AskMe.Service.Models;

namespace AskMe.Service.Services;

public interface IFeedService
{
    Task<PostResponse[]> Select(string userLogin, DateTime? timeAfter = null);
    Task<PostResponse> Read(Guid postId);
    Task<Result> CreateOrUpdate(PostRequest request, Guid? postId = null);
    Task<Result> Delete(Guid postId);
    Result Buy(Guid postId);
    Task<Dictionary<Guid, bool>> IsUserHaveAccessByPostId(string userLogin, Guid[] postIds);
}
