using AskMe.Core.Models.Dbo;
using AskMe.Service.Models;

namespace AskMe.Service.Converters;

public class PostConverter : IPostConverter
{
    public PostResponse Convert(Post post)
    {
        return new PostResponse
        {
            Id = post.Id,
            CreateAt = post.CreatedAt,
            Content = post.Content,
            SubscriptionId = post.SubscriptionId,
            Title = post.Title,
            AuthorId = post.AuthorId
        };
    }

    public Post Convert(Guid postId, Guid authorId, DateTime createdAt, PostRequest request)
    {
        return new Post
        {
            Id = postId,
            AuthorId = authorId,
            Content = request.Content!,
            CreatedAt = createdAt,
            SubscriptionId = request.SubscriptionId,
            Title = request.Title
        };
    }
}
