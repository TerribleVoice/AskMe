using System.Security.Claims;
using AskMe.Core.Models;
using AskMe.Service.Models;
using AskMe.Service.Services;
using AskMe.WebApi.Builders;
using AskMe.WebApi.Models;
using Microsoft.AspNetCore.Authentication;
using Microsoft.AspNetCore.Authentication.Cookies;
using Microsoft.AspNetCore.Authorization;
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
    public async Task<IActionResult> CreateAsync([FromBody]UserCreationForm creationForm)
    {
        await userService.CreateUserAsync(creationForm);
        return Ok();
    }

    [HttpPost("update")]
    [Authorize]
    public async Task<IActionResult> UpdateAsync([FromBody] UserUpdateForm updateForm)
    {
        if (CurrentUser == null || CurrentUser.Login != updateForm.Login)
        {
            return Forbid();
        }

        await userService.UpdateUserAsync(updateForm);
        return Ok();
    }

    [HttpPost("login")]
    public async Task<IActionResult> Login([FromBody]UserLoginForm form, string? returnUrl)
    {
        if ((await userService.AuthenticateUserAsync(form.Login, form.Password)).IsSuccess)
        {
            var user = await userService.ReadUserByLoginAsync(form.Login);

            var claims = new List<Claim>
            {
                new("/id", user.Id.ToString()),
                new(ClaimTypes.Name, form.Login),
                new(ClaimTypes.Email, user.Email ?? string.Empty),
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
    public async Task<ActionResult<UserViewModel>> GetUserProfile(string userLogin)
    {
        try
        {
            await userService.ReadUserByLoginAsync(userLogin);
        }
        catch (Exception e)
        {
            NotFound(e.Message);
        }

        return Ok(await userViewModelBuilder.Build(userLogin));
    }

    [HttpGet("top_authors")]
    public async Task<UserViewModel[]> GetTopAuthors(int limit)
    {
        var authorsDtos = await userService.GetTopAuthorsAsync(limit);

        return authorsDtos.Select(x => new UserViewModel(x)).ToArray();
    }
}
