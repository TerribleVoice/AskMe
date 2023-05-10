using System.Security.Claims;
using AskMe.Core.Models;
using AskMe.Service.Models;
using AskMe.Service.Services;
using AskMe.WebApi.Builders;
using AskMe.WebApi.Models;
using Microsoft.AspNetCore.Authentication;
using Microsoft.AspNetCore.Authentication.Cookies;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Cors;
using Microsoft.AspNetCore.Mvc;

namespace AskMe.WebApi.Controllers;

[ApiController]
[Route("[controller]")]
public class UserController : CustomControllerBase
{
    private readonly IUserService userService;
    private readonly UserViewModelBuilder userViewModelBuilder;

    public UserController(IUserIdentity userIdentity, IUserService userService, UserViewModelBuilder userViewModelBuilder) : base(userIdentity)
    {
        this.userService = userService;
        this.userViewModelBuilder = userViewModelBuilder;
    }

    [HttpPost("create")]
    public async Task<IActionResult> CreateAsync(UserCreationForm creationForm)
    {
        var creationResult = await userService.CreateUser(creationForm);
        return ProcessResult(creationResult);
    }

    [HttpPost("login")]
    public async Task<IActionResult> Login(string login, string password, string? returnUrl)
    {
        if ((await userService.AuthenticateUser(login, password)).IsSuccess)
        {
            var userResult = await userService.FindUserByLogin(login);
            if (userResult.IsFailure)
            {
                return BadRequest(userResult.ErrorMsg);
            }
            var user = userResult.Value!;
            var claims = new List<Claim>
            {
                new("/id", user.Id.ToString()),
                new(ClaimTypes.Name, login),
                new(ClaimTypes.Email, user.Email ?? string.Empty),
                new(ClaimTypes.Role, user.IsAuthor ? Roles.Author : Roles.Reader),
            };
            var claimIdentity = new ClaimsIdentity(claims, "Cookies");
            await HttpContext.SignInAsync(CookieAuthenticationDefaults.AuthenticationScheme, new ClaimsPrincipal(claimIdentity));

            return Ok(true);
        }

        return Unauthorized();
    }

    [HttpGet("logout")]
    [Authorize]
    public async Task<IActionResult> Logout()
    {
        if (CurrentUser == null)
        {
            BadRequest("Невозможно выйти, потому что пользователь не авторизован");
        }

        await HttpContext.SignOutAsync(CookieAuthenticationDefaults.AuthenticationScheme);
        return Ok();
    }

    [HttpGet("{userLogin}")]
    public async Task<IActionResult> GetUserProfile(string userLogin)
    {
        var user = await userService.FindUserByLogin(userLogin);
        if (user.IsFailure)
        {
            return NotFound(user.ErrorMsg);
        }
        return Ok(await userViewModelBuilder.Build(userLogin));
    }

    [HttpGet("get_current_user_only_for_test"), Authorize]
    [Obsolete]
    public IActionResult GetUser()
    {
        var user = User;
        return Ok(new {user.Identity.IsAuthenticated, user.Identity.Name});
    }
}
