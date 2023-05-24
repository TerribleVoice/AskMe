using AskMe.Service.Models;

namespace AskMe.WebApi.Models;

public class PostViewModel
{
    public Guid Id { get; set; }
    public string? Content { get; set; }
    public DateTime CreateAt { get; set; }
    public bool HaveAccess { get; set; }

    public UserViewModel AuthorViewModel { get; set; }

    public static PostViewModel CreateNoAccess(PostResponse post, UserViewModel authorViewModel)
    {
        return new PostViewModel
        {
            HaveAccess = false,
            Id = post.Id,
            Content = null,
            CreateAt = post.CreateAt,
            AuthorViewModel = authorViewModel
        };
    }

    public static PostViewModel CreateHaveAccess(PostResponse post, UserViewModel authorViewModel)
    {
        return new PostViewModel
        {
            HaveAccess = true,
            Id = post.Id,
            Content = post.Content,
            CreateAt = post.CreateAt,
            AuthorViewModel = authorViewModel
        };
    }
}
