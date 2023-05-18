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

    public async Task<PostViewModel[]> BuildUserPostsAsync(string userLogin)
    {
        var posts = await feedService.GetUserPostsAsync(userLogin);
        var accessMap = await feedService.IsUserHaveAccessToPostsAsync(userLogin, posts);

        return posts.Select(post => accessMap[post.Id]
                ? PostViewModel.CreateHaveAccess(post)
                : PostViewModel.CreateNoAccess(post))
            .ToArray();
    }
}
