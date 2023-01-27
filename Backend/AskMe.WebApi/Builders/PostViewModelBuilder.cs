using AskMe.Service.Services;
using AskMe.WebApi.Models;

namespace AskMe.WebApi.Builders;

public class PostViewModelBuilder
{
    private readonly IFeedService feedService;

    public PostViewModelBuilder(IFeedService feedService)
    {
        this.feedService = feedService;
    }

    public async Task<PostViewModel[]> BuildUserPosts(string userLogin)
    {
        var userPosts = await feedService.Select(userLogin);
        var haveAccessToPost = await feedService.IsUserHaveAccessByPostId(userLogin, userPosts.Select(x => x.Id).ToArray());
        return userPosts.Select(x => haveAccessToPost[x.Id]
                ? PostViewModel.CreateHaveAccess(x)
                : PostViewModel.CreateNoAccess(x))
            .ToArray();
    }
}
