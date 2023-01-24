using AskMe.Service.Models;
using AskMe.Service.Services;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Cors;
using Microsoft.AspNetCore.Mvc;

namespace AskMe.WebApi.Controllers;

[ApiController]
[EnableCors("MyPolicy")]
[Route("[controller]")]
public class FeedController : CustomControllerBase
{
    private readonly IFeedService feedService;
    private readonly IUserIdentity userIdentity;

    public FeedController(IFeedService feedService, IUserIdentity userIdentity) : base(userIdentity)
    {
        this.feedService = feedService;
        this.userIdentity = userIdentity;
    }

    [HttpGet("{userLogin}/feed")]
    [Authorize]
    public async Task<PostResponse[]> ShowFeed(string userLogin)
    {
        return await feedService.Select(userLogin);
    }

    [HttpGet("{postId:guid}")]
    [Authorize]
    public async Task<PostResponse> GetPost(Guid postId)
    {
        return await feedService.Read(postId);
    }

    [HttpGet("{userLogin}/feed_after")]
    [Authorize]
    public async Task<PostResponse[]> FeedAfter(string userLogin, DateTime timeAfter)
    {
        return await feedService.Select(userLogin, timeAfter);
    }

    [HttpPost("create")]
    [Authorize]
    public async Task<IActionResult> Create([FromBody] PostRequest request)
    {
        AssertUserIsAuthor();
        var creationResult =  await feedService.CreateOrUpdate(request);

        return ProcessResult(creationResult);
    }

    [HttpDelete("{postId:guid}")]
    [Authorize]
    public async Task<IActionResult> Delete(Guid postId)
    {
        AssertUserIsAuthor();
        var deletionResult = await feedService.Delete(postId);

        return ProcessResult(deletionResult);
    }

    [HttpPost("{postId:guid}/update")]
    [Authorize]
    public async Task<IActionResult> Update(Guid postId, [FromBody] PostRequest request)
    {
        AssertUserIsAuthor();
        var updateResult =  await feedService.CreateOrUpdate(request, postId);

        return ProcessResult(updateResult);
    }

    [HttpGet("{postId:guid}/buy")]
    [Authorize]
    public IActionResult BuyPost(Guid postId)
    {
        AssertUserIsReader();
        throw new NotImplementedException();
    }


}
