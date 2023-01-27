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
    public string? QiwiToken { get; set; }
    public string? Description { get; set; }
    public string? Links { get; set; }

}
