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
        var userResult = await userService.FindUserByLogin(userLogin);
        if (userResult.IsFailure)
        {
            throw new Exception(userResult.ErrorMsg);
        }
        var result = await postRepository.Select(userResult.Value!.Id, timeAfter);
        return result.Select(postConverter.Convert).ToArray();
    }

    public async Task<PostResponse> Read(Guid postId)
    {
        var readResult = await postRepository.Read(postId);
        if (readResult.IsFailure)
        {
            throw new ArgumentException(readResult.ErrorMsg);
        }

        return postConverter.Convert(readResult.Value!);
    }

    public async Task<Result> CreateOrUpdate(PostRequest request, Guid? postId = null)
    {
        var id = postId ?? Guid.NewGuid();
        var authorId = userIdentity.CurrentUser.Id;
        var postDbo = postConverter.Convert(id, authorId, DateTime.Now, request);

        return postId.HasValue
            ? await postRepository.Update(postDbo)
            : await postRepository.Create(postDbo);
    }

    public async Task<Result> Delete(Guid postId)
    {
        return await postRepository.Delete(postId);
    }

    public Result Buy(Guid postId)
    {
        throw new NotImplementedException();
    }
}
