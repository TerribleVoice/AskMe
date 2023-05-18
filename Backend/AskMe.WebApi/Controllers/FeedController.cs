using AskMe.Service.Models;
using AskMe.Service.Services;
using AskMe.WebApi.Builders;
using AskMe.WebApi.Models;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;

namespace AskMe.WebApi.Controllers;

[ApiController]
[Route("[controller]")]
public class FeedController : CustomControllerBase
{
    private readonly IFeedService feedService;
    private readonly IUserService userService;
    private readonly PostViewModelBuilder postViewModelBuilder;

    public FeedController(IFeedService feedService,
        IUserService userService,
        IUserIdentity userIdentity,
        PostViewModelBuilder postViewModelBuilder
        ) : base(userIdentity)
    {
        this.feedService = feedService;
        this.userService = userService;
        this.postViewModelBuilder = postViewModelBuilder;
    }

    [HttpGet("{userLogin}/feed")]
    [Authorize]
    public async Task<PostResponse[]> GetUserFeed(string userLogin)
    {
        return await feedService.GetFeedAsync(userLogin);
    }

    public async Task<ActionResult<PostViewModel[]>> GetUserPosts(string userLogin)
    {
        try
        {
            await userService.ReadUserByLoginAsync(userLogin);
        }
        catch (Exception e)
        {
            NotFound(e.Message);
        }

        var posts = await postViewModelBuilder.BuildUserPostsAsync(userLogin);
        return posts;
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
        return await feedService.GetFeedAsync(userLogin, timeAfter);
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
