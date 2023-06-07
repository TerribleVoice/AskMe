using AskMe.Core.Models;
using AskMe.Service.Models;
using AskMe.Service.Services;
using AskMe.WebApi.Models;

namespace AskMe.WebApi.Builders;

public class PostViewModelBuilder
{
    private readonly UserViewModelBuilder userViewModelBuilder;
    private readonly IFeedService feedService;
    private readonly IUserIdentity userIdentity;
    private readonly IUserService userService;

    public PostViewModelBuilder(UserViewModelBuilder userViewModelBuilder,
        IFeedService feedService,
        ISubscriptionService subscriptionService,
        IUserIdentity userIdentity,
        IUserService userService
    )
    {
        this.userViewModelBuilder = userViewModelBuilder;
        this.feedService = feedService;
        this.userIdentity = userIdentity;
        this.userService = userService;
    }

    public async Task<PostViewModel[]> BuildAsync(PostResponse[] posts)
    {
        var readerLogin = userIdentity.CurrentUser == null ? "" : userIdentity.CurrentUser.Login;
        var accessMap = await feedService.IsUserHaveAccessToPostsAsync(readerLogin, posts);

        var authorsByPostIds = new Dictionary<Guid, UserDto>();
        foreach (var post in posts)
        {
            var author = await userService.ReadUserByIdAsync(post.AuthorId);
            authorsByPostIds.Add(post.Id, author);
        }
        var postAttachments = await GetPostAttachments(posts);

        var results = new List<PostViewModel>();
        foreach (var post in posts)
        {
            var authorViewModel = await userViewModelBuilder.BuildAsync(authorsByPostIds[post.Id]);
            if (accessMap[post.Id])
                results.Add(PostViewModel.CreateHaveAccess(post, authorViewModel, postAttachments[post.Id]));
            else
                PostViewModel.CreateNoAccess(post, authorViewModel, postAttachments[post.Id]);
        }
        return results.ToArray();
    }

    private async Task<Dictionary<Guid, AttachmentResponse[]>> GetPostAttachments(PostResponse[] posts)
    {
        return (await Task.WhenAll(posts.Select(async x =>
                new { x.Id, Attachments = await feedService.GetPostAttachmentUrlsAsync(x.Id) }
            )))
            .ToDictionary(x => x.Id, x => x.Attachments);
    }
}
