using AskMe.Core.Models;
using AskMe.Core.StorageLayer.Repositories;
using AskMe.Service.Converters;
using AskMe.Service.Models;

namespace AskMe.Service.Services;

public class FeedService : IFeedService
{
    private readonly IPostRepository postRepository;
    private readonly IUserService userService;
    private readonly IPostConverter postConverter;
    private readonly IUserIdentity userIdentity;

    public FeedService(
        IPostRepository postRepository,
        IUserService userService,
        IPostConverter postConverter,
        IUserIdentity userIdentity
        )
    {
        this.postRepository = postRepository;
        this.userService = userService;
        this.postConverter = postConverter;
        this.userIdentity = userIdentity;
    }

    public async Task<PostResponse[]> Select(string userLogin, DateTime? timeAfter = null)
    {
        var userResult = (await userService.FindUserByLogin(userLogin)).ThrowIfFailure();

        var result = await postRepository.SelectByAuthorId(userResult.Id, timeAfter);
        return result.Select(postConverter.Convert).ToArray();
    }

    public async Task<PostResponse> Read(Guid postId)
    {
        var readResult = (await postRepository.Read(postId)).ThrowIfFailure();

        return postConverter.Convert(readResult);
    }

    public async Task<Result> CreateOrUpdate(PostRequest request, Guid? postId = null)
    {
        if (postId.HasValue)
        {
            var canBeEditedResult = await CanBeEdited(postId.Value);
            if (canBeEditedResult.IsFailure)
            {
                return canBeEditedResult;
            }
        }

        var id = postId ?? Guid.NewGuid();
        var authorId = userIdentity.CurrentUser!.Id;
        var postDbo = postConverter.Convert(id, authorId, DateTime.Now, request);

        return postId.HasValue
            ? await postRepository.Update(postDbo)
            : await postRepository.Create(postDbo);
    }

    private async Task<Result> CanBeEdited(Guid postId)
    {
        var readResult = await postRepository.Read(postId);
        if (readResult.IsFailure)
        {
            return readResult;
        }

        return readResult.Value!.AuthorId == userIdentity.CurrentUser!.Id
            ? Result.Ok()
            : Result.Fail("Авторизованный пользователь не является автором поста. Он не имет прав на действия с постом");
    }

    public async Task<Result> Delete(Guid postId)
    {
        var canBeEditedResult = await CanBeEdited(postId);
        if (canBeEditedResult.IsFailure)
        {
            return canBeEditedResult;
        }

        return await postRepository.Delete(postId);
    }

    public async Task<Dictionary<Guid, bool>> IsUserHaveAccessByPostId(string userLogin, Guid[] postIds)
    {
        var userPosts = await postRepository.SelectByIds(postIds);
        //todo доделать проверку доступов
        return userPosts.ToDictionary(x => x.Id, _=> true);
    }

    public Result Buy(Guid postId)
    {
        throw new NotImplementedException();
    }
}
