namespace AskMe.WebApi.Models;

public class UserCreationForm
{
    public UserCreationForm()
    {
        Login = string.Empty;
        Password = string.Empty;
    }

    public string Login { get; set; }

    public string? Email { get; set; }

    public string Password { get; set; }

    public bool IsAuthor { get; set; }
}
