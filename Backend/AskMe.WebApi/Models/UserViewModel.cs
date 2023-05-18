namespace AskMe.WebApi.Models;

public class UserViewModel
{
    public UserViewModel()
    {
        Login = string.Empty;
    }

    public string Login { get; set; }
    public string? Description { get; set; }
    public string? Links { get; set; }
}
