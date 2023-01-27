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
        var userDto = (await userService.FindUserByLogin(userLogin)).ThrowIfFailure();

        var userViewModel = new UserViewModel
        {
            Description = userDto.Description,
            IsAuthor = userDto.IsAuthor,
            Links = userDto.Links,
            Login = userLogin
        };

        if (!userDto.IsAuthor)
        {
            return userViewModel;
        }

        userViewModel.Posts = await postViewModelBuilder.BuildUserPosts(userLogin);
        return userViewModel;
    }
}
