using AskMe.Core.Models;
using AskMe.Core.Models.Dbo;
using AskMe.Core.StorageLayer;
using AskMe.Service.Converters;
using AskMe.Service.Models;
using AskMe.WebApi.Models;
using Microsoft.EntityFrameworkCore;

namespace AskMe.Service.Services;

public class FeedService : IFeedService
{
    private readonly PostgresDbContext dbContext;
    private readonly IUserService userService;
    private readonly IPostConverter postConverter;
    private readonly IUserIdentity userIdentity;
    private readonly ISubscriptionService subscriptionService;
    private readonly IS3StorageHandler s3StorageHandler;

    public FeedService(
        PostgresDbContext dbContext,
        IUserService userService,
        IPostConverter postConverter,
        IUserIdentity userIdentity,
        ISubscriptionService subscriptionService,
        IS3StorageHandler s3StorageHandler
        )
    {
        this.dbContext = dbContext;
        this.userService = userService;
        this.postConverter = postConverter;
        this.userIdentity = userIdentity;
        this.subscriptionService = subscriptionService;
        this.s3StorageHandler = s3StorageHandler;
    }

    public async Task<PostResponse[]> GetFeedAsync(string userLogin, DateTime? timeAfter = null)
    {
        var subscriptionIds = (await subscriptionService.GetReaderSubscriptionsFlatTreeAsync(userLogin)).Select(x=>x.Id).ToArray();

        var posts = await dbContext.Posts
            .Where(x=>subscriptionIds.Contains(x.SubscriptionId))
            .OrderByDescending(x => x.CreatedAt)
            .FilterByTime(timeAfter)
            .ToArrayAsync();

        return posts.Select(postConverter.Convert).ToArray();
    }

    public async Task<PostResponse> ReadAsync(Guid postId)
    {
        var post = await dbContext.ReadAsync<Post>(postId);

        return postConverter.Convert(post);
    }

    public async Task<PostResponse[]> GetUserPostsAsync(string userLogin)
    {
        var posts = await dbContext.Users
            .Where(x => x.Login == userLogin)
            .SelectMany(x => x.Posts)
            .ToArrayAsync();

        return posts.Select(x => postConverter.Convert(x)).ToArray();
    }

    public async Task AttachFilesAsync(Guid postId, AttachmentRequest[] attachmentRequests)
    {
        if (await dbContext.CanCurrentUserEdit<Post>(postId))
        {
            throw new Exception($"У {userIdentity.CurrentUser!.Login} доступа на редактирование поста {postId}");
        }

        var tasks = new List<Task>();
        foreach (var request in attachmentRequests)
        {
            var stream = request.FileStream;
            var path = S3StorageHandler.CreatePath("posts", postId.ToString(), $"{request.Type.ToString().ToLower()}-{request.Name}");
            tasks.Add(s3StorageHandler.UploadFileAsync(stream, path));
        }

        await Task.WhenAll(tasks);
    }

    public async Task<AttachmentResponse[]> GetPostAttachmentUrls(Guid postId)
    {
        var path = S3StorageHandler.CreatePath("posts", postId.ToString());
        var fileKeys =  await s3StorageHandler.GeFileKeysInDirectoryAsync(path);


        var fileNames = fileKeys.ToDictionary(
            x => x,
            key => key.Split('/').Last()
        );
        return fileKeys.Select(fileKey => new AttachmentResponse
        {
            FileType = AttachmentService.GetFileType(fileNames[fileKey]),
            SourceUrl = s3StorageHandler.GetFileUrl(fileKey)
        }).ToArray();
    }

    public async Task<Guid> CreateOrUpdateAsync(PostRequest request, Guid? postId = null)
    {
        var id = postId ?? Guid.NewGuid();
        var authorId = userIdentity.CurrentUser!.Id;
        var postDbo = postConverter.Convert(id, authorId, DateTime.Now, request);
        postDbo.TimeToUtc();

        if (postId.HasValue)
        {
            dbContext.Posts.Update(postDbo);
        }
        else
        {
            dbContext.Posts.Add(postDbo);
        }

        await dbContext.SaveChangesAsync();
        return postDbo.Id;
    }

    public async Task DeleteAsync(Guid postId)
    {
        await ThrowIfCantEdit(postId);

        var post = await dbContext.ReadAsync<Post>(postId);
        dbContext.Posts.Remove(post);
        await dbContext.SaveChangesAsync();
    }

    public async Task<Dictionary<Guid, bool>> IsUserHaveAccessToPostsAsync(string userLogin, PostResponse[] posts)
    {
        var userSubscriptions = await subscriptionService.GetReaderSubscriptionsFlatTreeAsync(userLogin);

        return posts.ToDictionary(
            post => post.Id,
            post => userSubscriptions.Any(subscription => post.SubscriptionId == subscription.Id));
    }

    // public async Task<>

    private async Task ThrowIfCantEdit(Guid postId)
    {
        var readResult = await dbContext.Posts.FirstAsync(x => x.Id == postId);

        if (readResult.AuthorId != userIdentity.CurrentUser!.Id)
        {
            throw new Exception("Авторизованный пользователь не является автором поста. Он не имет прав на действия с постом");
        }
    }
}
