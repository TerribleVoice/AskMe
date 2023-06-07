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

    public async Task<UserViewModel> BuildAsync(string userLogin)
    {
        var userDto = await userService.ReadUserByLoginAsync(userLogin);

        return await BuildAsync(userDto);
    }

    public async Task<UserViewModel> BuildAsync(UserDto userDto)
    {
        var profileImageUrl = await userService.GetUserProfileImageUrlAsync(userDto.Login);

        return new UserViewModel
        {
            Description = userDto.Description,
            Links = userDto.Links,
            Login = userDto.Login,
            ProfileImageUrl = profileImageUrl
        };
    }
}
