using System.Security.Claims;
using AskMe.Core.Models;
using AskMe.Service.Models;
using AskMe.Service.Services;
using AskMe.WebApi.Models;
using Microsoft.AspNetCore.Authentication;
using Microsoft.AspNetCore.Authentication.Cookies;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;

namespace AskMe.WebApi.Controllers;

[ApiController]
[Route("[controller]")]
public class UserController : ControllerBase
{
    private readonly ILogger<UserController> _logger;
    private readonly IUserService userService;

    public UserController(ILogger<UserController> logger, IUserService userService)
    {
        this.userService = userService;
        _logger = logger;
    }

    [HttpGet(Name = "GetUsersList")]
    public IEnumerable<UserDto> GetUsersList()
    {
        var users = userService.GetAll();
        return users.Value!;
    }

    [HttpPost("Create")]
    public async Task<IActionResult> CreateAsync(UserCreationForm creationForm)
    {
        try
        {
            await userService.CreateUser(creationForm);
        }
        catch (Exception e)
        {
            _logger.LogError(e.Message);
            return BadRequest("Не удалось зарегистрировать пользователя, попробуйте еще раз");
        }
        return Ok();
    }

    [HttpPost("Login")]
    public async Task<IActionResult> Login(string login, string password, string? returnUrl)
    {
        if ((await userService.AuthenticateUser(login, password)).IsSuccess)
        {
            var userResult = await userService.GetUser(login);
            if (userResult.IsFailure)
            {
                return BadRequest(userResult.ErrorMsg);
            }
            var userRole = userResult.Value!.IsAuthor ? Roles.Author : Roles.Reader;
            var claims = new List<Claim> { new(ClaimTypes.Name, login), new(ClaimTypes.Role, userRole) };
            var claimIdentity = new ClaimsIdentity(claims, "Cookies");
            await HttpContext.SignInAsync(CookieAuthenticationDefaults.AuthenticationScheme, new ClaimsPrincipal(claimIdentity));
            return Ok(true);
        }

        return Unauthorized();
    }

    [HttpGet("GetUser"), Authorize]
    public IActionResult GetUser()
    {
        var user = User;
        return Ok(new {user.Identity.IsAuthenticated, user.Identity.Name});
    }
}
