using AskMe.Service.Models;
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

    public async Task<PostViewModel[]> BuildAsync(PostResponse[] posts, string userLogin)
    {
        var accessMap = await feedService.IsUserHaveAccessToPostsAsync(userLogin, posts);

        var authorViewModel = await userViewModelBuilder.BuildAsync(userLogin);
        var postAttachments = await GetPostAttachments(posts);
        return posts.Select(post => accessMap[post.Id]
                ? PostViewModel.CreateHaveAccess(post, authorViewModel, postAttachments[post.Id])
                : PostViewModel.CreateNoAccess(post, authorViewModel, postAttachments[post.Id]))
            .ToArray();
    }

    private async Task<Dictionary<Guid, AttachmentResponse[]>> GetPostAttachments(PostResponse[] posts)
    {
        return (await Task.WhenAll(posts.Select(async x =>
                new { x.Id, Attachments = await feedService.GetPostAttachmentUrlsAsync(x.Id) }
            )))
            .ToDictionary(x => x.Id, x => x.Attachments);
    }
}
