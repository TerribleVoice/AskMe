using AskMe.Core.Models;
using AskMe.Service.Models;
using AskMe.Service.Services;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;

namespace AskMe.WebApi.Controllers;

[ApiController]
[Route("[controller]")]
public class SubscriptionController : CustomControllerBase
{
    private readonly ISubscriptionService subscriptionService;

    public SubscriptionController(IUserIdentity userIdentity, ISubscriptionService subscriptionService) : base(userIdentity)
    {
        this.subscriptionService = subscriptionService;
    }

    [HttpPost("create")]
    [Authorize]
    public async Task<IActionResult> Create([FromBody] SubscriptionRequest subscriptionRequest)
    {
        await subscriptionService.CreateOrUpdateAsync(subscriptionRequest);
        return Ok();
    }

    [HttpDelete("delete")]
    [Authorize]
    public async Task<IActionResult> Delete(Guid id)
    {
        await subscriptionService.DeleteAsync(id);
        return Ok();
    }

    [HttpPost("{subscriptionId}/update")]
    [Authorize]
    public async Task<IActionResult> Update(Guid subscriptionId, [FromBody] SubscriptionRequest subscriptionRequest)
    {
        await subscriptionService.CreateOrUpdateAsync(subscriptionRequest, subscriptionId);
        return Ok();
    }

    //Метод для авторов, показывает подписки созданные пользователем

    [HttpGet("{userLogin}/created_list")]
    [Authorize]
    public async Task<SubscriptionResponse[]> AuthorSubscriptions(string userLogin)
    {
        var subscriptions = await subscriptionService.GetAuthorSubscriptionsAsync(userLogin);
        return subscriptions;
    }

    [HttpGet("subscriptions_without_children")]
    [Authorize]
    public async Task<ActionResult<SubscriptionResponse[]>> SubscriptionsWithoutChildren(string userLogin)
    {
        var result = await subscriptionService.SubscriptionsWithoutChildrenAsync(userLogin);

        return Ok(result);
    }


    //Метод для читателей, показывает купленные подписки

    [HttpGet("{userLogin}/bought_list")]
    [Authorize]
    public async Task<SubscriptionResponse[]> UserSubscriptions(string userLogin)
    {
        var subscriptions = await subscriptionService.GetReaderSubscriptionsAsync(userLogin);
        return subscriptions;
    }

    [HttpGet("{id:guid}/subscribe")]
    [Authorize]
    public async Task<IActionResult> Subscribe(Guid id)
    {
        await subscriptionService.SubscribeAsync(id);
        return Ok();
    }

    [HttpGet("{id:guid}/unsubscribe")]
    [Authorize]
    public async Task<IActionResult> Unsubscribe(Guid id)
    {
        await subscriptionService.UnsubscribeAsync(id);
        return Ok();
    }
}
