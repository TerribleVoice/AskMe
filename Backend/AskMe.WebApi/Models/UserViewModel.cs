namespace AskMe.WebApi.Models;

public class UserViewModel
{
    public UserViewModel()
    {
        // Posts = Array.Empty<PostViewModel>();
        Login = string.Empty;
    }

    public string Login { get; set; }
    public string? Description { get; set; }
    public string? Links { get; set; }
    // public PostViewModel[] Posts { get; set; }
}
