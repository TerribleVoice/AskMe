namespace AskMe.Service.Models;

public class UserCreationDto : UserDto
{
    public UserCreationDto()
    {
        Password = string.Empty;
    }

    public string Password { get; set; }
}
