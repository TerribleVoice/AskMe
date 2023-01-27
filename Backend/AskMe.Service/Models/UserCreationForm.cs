namespace AskMe.Service.Models;

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
    public string? QiwiToken { get; set; }
    public string? Description { get; set; }
    public string? Links { get; set; }

}
