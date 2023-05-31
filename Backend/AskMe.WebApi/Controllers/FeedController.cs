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
    public async Task<ActionResult<PostViewModel[]>> GetUserFeed(string userLogin, int skip = 0, int take = 10)
    {
        var posts = await feedService.GetFeedAsync(userLogin, skip, take);
        var postsViewModels = await postViewModelBuilder.BuildAsync(posts, userLogin);

        return postsViewModels;
    }

    [HttpGet("{userLogin}/posts")]
    public async Task<ActionResult<PostViewModel[]>> GetUserPosts(string userLogin, int skip = 0, int take = 10)
    {
        var posts = await feedService.GetUserPostsAsync(userLogin, skip, take);
        var postViewModels = await postViewModelBuilder.BuildAsync(posts, userLogin);

        return postViewModels;
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
