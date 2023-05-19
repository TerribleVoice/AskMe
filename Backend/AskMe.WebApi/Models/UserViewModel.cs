using AskMe.Service.Models;

namespace AskMe.WebApi.Models;

public class UserViewModel
{
    public UserViewModel()
    {
        Login = string.Empty;
    }

    public UserViewModel(UserDto userDto)
    {
        Login = userDto.Login;
        Description = userDto.Description;
        Links = userDto.Links;
    }

    public string Login { get; set; }
    public string? Description { get; set; }
    public string? Links { get; set; }
}
