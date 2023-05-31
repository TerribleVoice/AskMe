using AskMe.Core.Models;
using AskMe.Service.Models;
using AskMe.Service.Services;
using AskMe.WebApi.Builders;
using AskMe.WebApi.Models;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;

namespace AskMe.WebApi.Controllers;

[ApiController]
[Route("api/[controller]")]
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
    public async Task<ActionResult<PostViewModel[]>> GetUserFeed(string userLogin)
    {
        var posts = Array.Empty<PostViewModel>();
        try
        {
            posts = await postViewModelBuilder.BuildUserFeedAsync(userLogin);
        }
        catch (Exception e)
        {
            NotFound(e.Message);
        }
        return posts;
    }

    [HttpGet("{userLogin}/posts")]
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
    public async Task<PostResponse> GetPost(Guid postId)
    {
        return await feedService.ReadAsync(postId);
    }

    [HttpPost("create")]
    [Authorize]
    public async Task<ActionResult<Guid>> Create([FromForm] PostRequest request, [FromForm] IFormFile[] attachments)
    {
        var createdId = await feedService.CreateOrUpdateAsync(request);
        await AttachFiles(createdId, attachments);
        return Ok(createdId);
    }

    [HttpPost("{postId:guid}/attachFiles")]
    public async Task<IActionResult> AttachFiles([FromForm]Guid postId, [FromForm] IFormFile[] files)
    {
        var attachmentRequests =  files.Select(file=>new AttachmentRequest
        {
            Name = file.FileName,
            Type = AttachmentService.GetFileType(file.ContentType),
            FileStream = file.OpenReadStream()
        }).ToArray();

        await feedService.AttachFilesAsync(postId, attachmentRequests);
        return Ok();
    }

    [HttpGet("{userLogin}/feed_after")]
    [Authorize]
    public async Task<ActionResult<PostViewModel[]>> FeedAfter(string userLogin, DateTime timeAfter)
    {
        var posts = Array.Empty<PostViewModel>();
        try
        {
            posts = await postViewModelBuilder.BuildUserFeedAsync(userLogin, timeAfter);
        }
        catch (Exception e)
        {
            NotFound(e.Message);
        }
        return posts;
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
}
