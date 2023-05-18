using AskMe.Service.Services;
using AskMe.WebApi.Models;

namespace AskMe.WebApi.Builders;

public class PostViewModelBuilder
{
    private readonly IFeedService feedService;
    private readonly ISubscriptionService subscriptionService;

    public PostViewModelBuilder(IFeedService feedService,
        ISubscriptionService subscriptionService)
    {
        this.feedService = feedService;
        this.subscriptionService = subscriptionService;
    }

    public async Task<PostViewModel[]> BuildUserPostsAsync(string userLogin)
    {
        var posts = await feedService.GetUserPostsAsync(userLogin);
        var accessMap = await feedService.IsUserHaveAccessToPostsAsync(userLogin, posts);

        return posts.Select(post => accessMap[post.Id]
                ? PostViewModel.CreateHaveAccess(post)
                : PostViewModel.CreateNoAccess(post))
            .ToArray();
    }

    public async Task<PostViewModel[]> BuildUserFeedAsync(string userLogin, DateTime? timeAfter = null)
    {
        var posts = await feedService.GetFeedAsync(userLogin, timeAfter);

        return posts.Select(PostViewModel.CreateHaveAccess).ToArray();
    }
}
