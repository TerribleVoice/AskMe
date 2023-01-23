using System.Security.Claims;
using AskMe.Core.Models;
using AskMe.Service.Models;
using AskMe.Service.Services;
using Microsoft.AspNetCore.Authentication;
using Microsoft.AspNetCore.Authentication.Cookies;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Cors;
using Microsoft.AspNetCore.Mvc;

namespace AskMe.WebApi.Controllers;

[ApiController]
[EnableCors("MyPolicy")]
[Route("[controller]")]
public class UserController : ControllerBase
{
    private readonly ILogger<UserController> _logger;
    private readonly IUserService userService;
    private readonly IUserIdentity userIdentity;

    public UserController(ILogger<UserController> logger, IUserService userService, IUserIdentity userIdentity)
    {
        this.userService = userService;
        this.userIdentity = userIdentity;
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

    [HttpGet("GetUser"), Authorize]
    public IActionResult GetUser()
    {
        var user = User;
        return Ok(new {user.Identity.IsAuthenticated, user.Identity.Name});
    }
}
