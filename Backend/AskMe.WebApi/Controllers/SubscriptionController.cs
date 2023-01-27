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
    public SubscriptionController(IUserIdentity userIdentity) : base(userIdentity)
    {
    }

    [HttpPost("/create")]
    [Authorize]
    public async Task Create([FromBody] SubscriptionRequest subscriptionRequest)
    {
        AssertUserIsAuthor();
        throw new NotImplementedException();
    }

    [HttpDelete("/delete")]
    [Authorize]
    public async Task Delete(Guid id)
    {
        AssertUserIsAuthor();
        throw new NotImplementedException();
    }

    [HttpPost("/update")]
    [Authorize]
    public async Task Update(Guid subscriptionId, [FromBody] SubscriptionRequest subscriptionRequest)
    {
        AssertUserIsAuthor();
        throw new NotImplementedException();
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
    public async Task AuthorSubscriptions(string userLogin)
    {
        AssertUserIsAuthor();
        throw new NotImplementedException();
    }

    //Метод для читателей, показывает купленные подписки
    [HttpGet("{userLogin}/bought_list")]
    [Authorize]
    public async Task UserSubscriptions(string userLogin)
    {
        AssertUserIsReader();
        throw new NotImplementedException();
    }

    [HttpGet("{id:guid}/unsubscribe")]
    [Authorize]
    public async Task Unsubscribe(Guid id)
    {
        AssertUserIsReader();
        throw new NotImplementedException();
    }


}
