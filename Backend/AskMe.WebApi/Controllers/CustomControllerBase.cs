using AskMe.Core.Models;
using AskMe.Service.Services;
using Microsoft.AspNetCore.Mvc;

namespace AskMe.WebApi.Controllers;

public class CustomControllerBase : ControllerBase
{
    private readonly IUserIdentity userIdentity;
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
