using AskMe.Core.Models;
using AskMe.Core.Models.Dbo;
using Microsoft.AspNetCore.Mvc;

namespace AskMe.WebApi.Controllers;

public class CustomControllerBase : ControllerBase
{
    private readonly IUserIdentity userIdentity;

    public CustomControllerBase(IUserIdentity userIdentity)
    {
        this.userIdentity = userIdentity;
    }

    protected User? CurrentUser => userIdentity.CurrentUser;

    protected IActionResult ProcessResult(Result operationResult)
    {
        if (operationResult.IsFailure)
        {
            return BadRequest(operationResult.ErrorMsg);
        }

        return Ok();
    }
}
