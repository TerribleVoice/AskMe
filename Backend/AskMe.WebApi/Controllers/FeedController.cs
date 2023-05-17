using AskMe.Service.Models;
using AskMe.Service.Services;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;

namespace AskMe.WebApi.Controllers;

[ApiController]
[Route("[controller]")]
public class FeedController : CustomControllerBase
{
    private readonly IFeedService feedService;

    public FeedController(IFeedService feedService, IUserIdentity userIdentity) : base(userIdentity)
    {
        this.feedService = feedService;
    }

    [HttpGet("{userLogin}/feed")]
    [Authorize]
    public async Task<PostResponse[]> ShowFeed(string userLogin)
    {
        return await feedService.SelectAsync(userLogin);
    }

    [HttpGet("{postId:guid}")]
    [Authorize]
    public async Task<PostResponse> GetPost(Guid postId)
    {
        return await feedService.ReadAsync(postId);
    }

    [HttpGet("{userLogin}/feed_after")]
    [Authorize]
    public async Task<PostResponse[]> FeedAfter(string userLogin, DateTime timeAfter)
    {
        return await feedService.SelectAsync(userLogin, timeAfter);
    }

    [HttpPost("create")]
    [Authorize]
    public async Task<IActionResult> Create([FromBody] PostRequest request)
    {
        await feedService.CreateOrUpdateAsync(request);
        return Ok();
    }

    [HttpDelete("{postId:guid}")]
    [Authorize]
    public async Task<IActionResult> Delete(Guid postId)
    {
        await feedService.DeleteAsync(postId);
        return Ok();
    }

    [HttpPost("{postId:guid}/update")]
    [Authorize]
    public async Task<IActionResult> Update(Guid postId, [FromBody] PostRequest request)
    {
        await feedService.CreateOrUpdateAsync(request, postId);
        return Ok();
    }

    [HttpGet("{postId:guid}/buy")]
    [Authorize]
    public IActionResult BuyPost(Guid postId)
    {
        throw new NotImplementedException();
    }
}
