using System.ComponentModel.DataAnnotations;
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


    protected void AssertUserLoginIs(string login)
    {
        if (CurrentUser == null || CurrentUser.Login != login)
        {
            throw new ValidationException($"Пользователь {CurrentUser?.Login} это не {login}");
        }
    }
}
