using AskMe.Core.Models;
using AskMe.Service.Models;
using AskMe.Service.Services;
using Microsoft.AspNetCore.Mvc;

namespace AskMe.WebApi.Controllers;

[ApiController]
[Route("[controller]")]
public class FeedController : ControllerBase
{
    private readonly IFeedService feedService;
    private readonly IUserIdentity userIdentity;

    public FeedController(IFeedService feedService, IUserIdentity userIdentity)
    {
        this.feedService = feedService;
        this.userIdentity = userIdentity;

    }

    [HttpGet("{userLogin}/feed")]
    public async Task<PostResponse[]> ShowFeed(string userLogin)
    {
        return await feedService.Select(userLogin);
    }

    [HttpGet("{postId:guid}")]
    public async Task<PostResponse> GetPost(Guid postId)
    {
        return await feedService.Read(postId);
    }

    [HttpGet("{userLogin}/feed_after")]
    public async Task<PostResponse[]> FeedAfter(string userLogin, DateTime timeAfter)
    {
        return await feedService.Select(userLogin, timeAfter);
    }

    [HttpPost("create")]
    public async Task<IActionResult> Create([FromBody] PostRequest request)
    {
        var creationResult =  await feedService.CreateOrUpdate(request);

        return ProcessResult(creationResult);
    }

    [HttpDelete("{postId:guid}")]
    public async Task<IActionResult> Delete(Guid postId)
    {
        var deletionResult = await feedService.Delete(postId);

        return ProcessResult(deletionResult);
    }

    [HttpPost("{postId:guid}/update")]
    public async Task<IActionResult> Update(Guid postId, [FromBody] PostRequest request)
    {
        var updateResult =  await feedService.CreateOrUpdate(request, postId);

        return ProcessResult(updateResult);
    }

    [HttpGet("{postId:guid}/buy")]
    public IActionResult BuyPost(Guid postId)
    {
        throw new NotImplementedException();
    }

    private IActionResult ProcessResult(Result operationResult)
    {
        if (operationResult.IsFailure)
        {
            return BadRequest(operationResult.ErrorMsg);
        }

        return Ok();
    }
}
