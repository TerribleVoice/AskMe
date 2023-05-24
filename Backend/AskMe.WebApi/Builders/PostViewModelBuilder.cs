using AskMe.Service.Services;
using AskMe.WebApi.Models;

namespace AskMe.WebApi.Builders;

public class PostViewModelBuilder
{
    private readonly UserViewModelBuilder userViewModelBuilder;
    private readonly IFeedService feedService;
    private readonly ISubscriptionService subscriptionService;

    public PostViewModelBuilder(UserViewModelBuilder userViewModelBuilder,
        IFeedService feedService,
        ISubscriptionService subscriptionService)
    {
        this.userViewModelBuilder = userViewModelBuilder;
        this.feedService = feedService;
        this.subscriptionService = subscriptionService;
    }

    public async Task<PostViewModel[]> BuildUserPostsAsync(string userLogin)
    {
        var posts = await feedService.GetUserPostsAsync(userLogin);
        var accessMap = await feedService.IsUserHaveAccessToPostsAsync(userLogin, posts);

        var authorViewModel = await userViewModelBuilder.Build(userLogin);
        return posts.Select(post => accessMap[post.Id]
                ? PostViewModel.CreateHaveAccess(post, authorViewModel)
                : PostViewModel.CreateNoAccess(post, authorViewModel))
            .ToArray();
    }

    public async Task<PostViewModel[]> BuildUserFeedAsync(string userLogin, DateTime? timeAfter = null)
    {
        var posts = await feedService.GetFeedAsync(userLogin, timeAfter);
        var authorViewModel = await userViewModelBuilder.Build(userLogin);

        return posts.Select(post => PostViewModel.CreateHaveAccess(post, authorViewModel)).ToArray();
    }
}
