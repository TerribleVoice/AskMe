using AskMe.Service.Models;

namespace AskMe.WebApi.Models;

public class PostViewModel
{
    public Guid Id { get; set; }
    public string? Content { get; set; }
    public uint? Price { get; set; }
    public DateTime CreateAt { get; set; }
    public bool HaveAccess { get; set; }

    public static PostViewModel CreateNoAccess(PostResponse post)
    {
        return new PostViewModel
        {
            HaveAccess = false,
            Id = post.Id,
            Content = null,
            Price = post.Price,
            CreateAt = post.CreateAt
        };
    }

    public static PostViewModel CreateHaveAccess(PostResponse post)
    {
        return new PostViewModel
        {
            HaveAccess = true,
            Id = post.Id,
            Content = post.Content,
            Price = null,
            CreateAt = post.CreateAt
        };
    }
}