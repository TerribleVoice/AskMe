using AskMe.Service.Models;
using AskMe.Service.Services;
using AskMe.WebApi.Models;

namespace AskMe.WebApi.Builders;

public class UserViewModelBuilder
{
    private readonly IUserService userService;

    public UserViewModelBuilder(IUserService userService)
    {
        this.userService = userService;
    }

    public async Task<UserViewModel> Build(string userLogin)
    {
        var userDto = await userService.ReadUserByLoginAsync(userLogin);

        var userViewModel = new UserViewModel
        {
            Description = userDto.Description,
            Links = userDto.Links,
            Login = userLogin
        };

        return userViewModel;
    }
}
