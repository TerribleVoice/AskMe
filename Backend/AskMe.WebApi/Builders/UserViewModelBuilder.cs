using AskMe.Service.Services;
using AskMe.WebApi.Models;

namespace AskMe.WebApi.Builders;

public class UserViewModelBuilder
{
    private readonly IUserService userService;
    private readonly PostViewModelBuilder postViewModelBuilder;

    public UserViewModelBuilder(IUserService userService,
        PostViewModelBuilder postViewModelBuilder)
    {
        this.userService = userService;
        this.postViewModelBuilder = postViewModelBuilder;
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
