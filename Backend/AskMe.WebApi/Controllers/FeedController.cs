using AskMe.Core.Models;
using AskMe.Core.Models.Dbo;
using AskMe.Service.Models;
using Microsoft.AspNetCore.Mvc;

namespace AskMe.WebApi.Controllers;

[ApiController]
[Route("[controller]")]
public class FeedController : ControllerBase
{
    [HttpGet("{userLogin}/feed")]
    public Post[] ShowFeed(string userLogin)
    {
        throw new NotImplementedException();
    }

    [HttpGet("{postId:guid}")]
    public Post GetPost(Guid postId)
    {
        throw new NotImplementedException();
    }

    [HttpGet("{userLogin}/feed_after")]
    public Post[] FeedAfter(string userLogin, DateTime timeAfter)
    {
        throw new NotImplementedException();
    }

    [HttpPost("{userLogin}/create")]
    public Result Create(string userLogin, [FromBody] CreatePostRequest request)
    {
        throw new NotImplementedException();
    }

    [HttpDelete("{postId:guid}")]
    public Result Delete(Guid postId)
    {
        throw new NotImplementedException();
    }

    [HttpGet("{postId:guid}/update")]
    public Result Update(Guid postId, [FromBody] CreatePostRequest request)
    {
        throw new NotImplementedException();
    }

    [HttpGet("{postId:guid}/buy")]
    public Result BuyPost(Guid postId)
    {
        throw new NotImplementedException();
    }
}
