namespace AskMe.Service.Models;

public class UserDto
{
    public UserDto()
    {
        Login = string.Empty;
    }

    public Guid Id { get; set; }

    public string Login { get; set; }

    public string? Email { get; set; }

    public bool IsAuthor { get; set; }
}
