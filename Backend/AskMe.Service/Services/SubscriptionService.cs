using AskMe.Core.Models;
using AskMe.Core.StorageLayer.Repositories;
using AskMe.Service.Converters;
using AskMe.Service.Models;

namespace AskMe.Service.Services;

public class SubscriptionService : ISubscriptionService
{
    private readonly ISubscriptionRepository subscriptionRepository;
    private readonly ISubscriptionConverter subscriptionConverter;
    private readonly IUserIdentity userIdentity;
    private readonly IUserService userService;
    private readonly IUserSubscriptionRepository userSubscriptionRepository;

    public SubscriptionService(ISubscriptionRepository subscriptionRepository,
        ISubscriptionConverter subscriptionConverter,
        IUserIdentity userIdentity,
        IUserService userService,
        IUserSubscriptionRepository userSubscriptionRepository)
    {
        this.subscriptionRepository = subscriptionRepository;
        this.subscriptionConverter = subscriptionConverter;
        this.userIdentity = userIdentity;
        this.userService = userService;
        this.userSubscriptionRepository = userSubscriptionRepository;
    }

    public async Task<Result> CreateOrUpdate(SubscriptionRequest request, Guid? subscriptionId = null)
    {
        if (subscriptionId.HasValue)
        {
            var canBeEditedResult = await CanBeEdited(subscriptionId.Value);
            if (canBeEditedResult.IsFailure)
            {
                return canBeEditedResult;
            }
        }

        var id = subscriptionId ?? Guid.NewGuid();
        var authorId = userIdentity.CurrentUser!.Id;
        var postDbo = subscriptionConverter.Convert(id, authorId, request);

        return subscriptionId.HasValue
            ? await subscriptionRepository.Update(postDbo)
            : await subscriptionRepository.Create(postDbo);
    }

    public async Task<Result> Delete(Guid id)
    {
        var canBeEditedResult = await CanBeEdited(id);
        if (canBeEditedResult.IsFailure)
        {
            return canBeEditedResult;
        }

        return await subscriptionRepository.Delete(id);
    }

    public async Task<SubscriptionResponse[]> GetAuthorSubscriptions(string userLogin)
    {
        var userResult = (await userService.FindUserByLogin(userLogin)).ThrowIfFailure();

        var result = await subscriptionRepository.SelectByAuthorId(userResult.Id);
        return result.Select(subscriptionConverter.Convert).ToArray();

    }

    public async Task<SubscriptionResponse[]> GetReaderSubscriptions(string userLogin)
    {
        var userResult = (await userService.FindUserByLogin(userLogin)).ThrowIfFailure();
        var subscriptionIds = await userSubscriptionRepository.SelectSubscriptionIdsByUserId(userResult.Id);
        var subscriptions = await subscriptionRepository.SelectByIds(subscriptionIds);

        return subscriptions.Select(subscriptionConverter.Convert).ToArray();
    }

    public async Task<Result> Subscribe(Guid userId, Guid subscriptionId)
    {
        return await userSubscriptionRepository.Create(userId, subscriptionId);
    }

    public async Task<Result> Unsubscribe(Guid userId, Guid subscriptionId)
    {
        return await userSubscriptionRepository.Delete(userId, subscriptionId);
    }

    private async Task<Result> CanBeEdited(Guid subscriptionId)
    {
        var readResult = await subscriptionRepository.Read(subscriptionId);
        if (readResult.IsFailure)
        {
            return readResult;
        }

        return readResult.Value!.AuthorId == userIdentity.CurrentUser!.Id
            ? Result.Ok()
            : Result.Fail("Авторизованный пользователь не является автором поста. Он не имет прав на действия с постом");
    }
}
