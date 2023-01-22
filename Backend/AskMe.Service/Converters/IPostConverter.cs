using AskMe.Core.Models.Dbo;
using AskMe.Service.Models;

namespace AskMe.Service.Converters;

public interface IPostConverter
{
    PostResponse Convert(Post post);
    Post Convert(Guid postId, Guid authorId, DateTime createdAt, PostRequest request);
}
