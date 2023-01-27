using AskMe.Service.Models;
using AskMe.Service.Services;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Cors;
using Microsoft.AspNetCore.Mvc;

namespace AskMe.WebApi.Controllers;

[ApiController]
[EnableCors("MyPolicy")]
[Route("[controller]")]
public class SubscriptionController : CustomControllerBase
{
    private readonly ISubscriptionService subscriptionService;

    public SubscriptionController(IUserIdentity userIdentity, ISubscriptionService subscriptionService) : base(userIdentity)
    {
        this.subscriptionService = subscriptionService;
    }

    [HttpPost("/create")]
    [Authorize]
    public async Task<IActionResult> Create([FromBody] SubscriptionRequest subscriptionRequest)
    {
        AssertUserIsAuthor();
        var creationResult = await subscriptionService.CreateOrUpdate(subscriptionRequest);
        return ProcessResult(creationResult);
    }

    [HttpDelete("/delete")]
    [Authorize]
    public async Task<IActionResult> Delete(Guid id)
    {
        AssertUserIsAuthor();
        var deletionResult = await subscriptionService.Delete(id);
        return ProcessResult(deletionResult);
    }

    [HttpPost("/update")]
    [Authorize]
    public async Task<IActionResult> Update(Guid subscriptionId, [FromBody] SubscriptionRequest subscriptionRequest)
    {
        AssertUserIsAuthor();
        var updateResult = await subscriptionService.CreateOrUpdate(subscriptionRequest, subscriptionId);
        return ProcessResult(updateResult);
    }

    [HttpGet("{id:guid}/buy")]
    [Authorize]
    public async Task BuySubscription(Guid id)
    {
        AssertUserIsReader();
        throw new NotImplementedException();
    }

    //Метод для авторов, показывает подписки созданные пользователем
    [HttpGet("{userLogin}/created_list")]
    [Authorize]
    public async Task<SubscriptionResponse[]> AuthorSubscriptions(string userLogin)
    {
        AssertUserIsAuthor();
        var subscriptions = await subscriptionService.GetAuthorSubscriptions(userLogin);
        return subscriptions;
    }

    //Метод для читателей, показывает купленные подписки
    [HttpGet("{userLogin}/bought_list")]
    [Authorize]
    public async Task<SubscriptionResponse[]> UserSubscriptions(string userLogin)
    {
        AssertUserIsReader();
        var subscriptions = await subscriptionService.GetReaderSubscriptions(userLogin);
        return subscriptions;
    }

    [HttpGet("{id:guid}/unsubscribe")]
    [Authorize]
    public async Task<IActionResult> Unsubscribe(Guid id)
    {
        AssertUserIsReader();
        var result = await subscriptionService.Unsubscribe(id);
        return ProcessResult(result);
    }


}
