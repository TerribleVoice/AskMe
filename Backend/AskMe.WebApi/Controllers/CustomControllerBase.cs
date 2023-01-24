using AskMe.Core.Models;
using AskMe.Service.Models;
using AskMe.Service.Services;
using Microsoft.AspNetCore.Mvc;

namespace AskMe.WebApi.Controllers;

public class CustomControllerBase : ControllerBase
{
    private readonly IUserIdentity userIdentity;
    protected UserDto? CurrentUser => userIdentity.CurrentUser;

    public CustomControllerBase(IUserIdentity userIdentity)
    {
        this.userIdentity = userIdentity;
    }
    protected IActionResult ProcessResult(Result operationResult)
    {
        if (operationResult.IsFailure)
        {
            return BadRequest(operationResult.ErrorMsg);
        }

        return Ok();
    }

    protected void AssertUserIsAuthor()
    {
        if (!userIdentity.CurrentUser.IsAuthor)
        {
            throw new Exception("Необходимо, чтобы текущий пользователь имел роль \"Автор\"");
        }
    }

    protected void AssertUserIsReader()
    {
        if (userIdentity.CurrentUser.IsAuthor)
        {
            throw new Exception("Необходимо, чтобы текущий пользователь не имел роль \"Автор\"");
        }
    }
}
