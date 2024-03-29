using System.Security.Claims;
using AskMe.Core.Models;
using AskMe.Service.Models;
using AskMe.Service.Services;
using AskMe.WebApi.Builders;
using AskMe.WebApi.Enums;
using AskMe.WebApi.Models;
using Microsoft.AspNetCore.Authentication;
using Microsoft.AspNetCore.Authentication.Cookies;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;

namespace AskMe.WebApi.Controllers;

[ApiController]
[Route("api/[controller]")]
public class UserController : CustomControllerBase
{
    private readonly IUserService userService;
    private readonly UserViewModelBuilder userViewModelBuilder;

    public UserController(IUserIdentity userIdentity,
        IUserService userService,
        UserViewModelBuilder userViewModelBuilder
    ) : base(userIdentity)
    {
        this.userService = userService;
        this.userViewModelBuilder = userViewModelBuilder;
    }

    [HttpPost("create")]
    public async Task<IActionResult> CreateAsync([FromBody]UserCreationForm creationForm)
    {
        await userService.CreateUserAsync(creationForm);
        await CreateCookieSession(creationForm.Login);
        return Ok();
    }

    [HttpPost("update")]
    [Authorize]
    public async Task<IActionResult> UpdateAsync([FromBody] UserUpdateForm updateForm)
    {
        try
        {
            AssertUserLoginIs(updateForm.OldLogin);
        }
        catch (Exception e)
        {
            return BadRequest(e.Message);
        }

        await userService.UpdateUserAsync(updateForm);
        return Ok();
    }

    [HttpPost("login")]
    public async Task<IActionResult> Login([FromBody]UserLoginForm form, string? returnUrl)
    {
        if ((await userService.AuthenticateUserAsync(form.Login, form.Password)).IsSuccess)
        {
            await CreateCookieSession(form.Login);

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

        return Ok(await userViewModelBuilder.BuildAsync(userLogin));
    }

    [HttpGet("top_authors")]
    public async Task<UserViewModel[]> GetTopAuthors(int limit)
    {
        var authorsDtos = await userService.GetTopAuthorsAsync(limit);

        var viewModels = new List<UserViewModel>();
        foreach (var userDto in authorsDtos)
            viewModels.Add(await userViewModelBuilder.BuildAsync(userDto));
        return viewModels.ToArray();
    }

    [HttpPost("{userLogin}/profile_image")]
    [Authorize]
    public async Task<IActionResult> UploadProfileImage(string userLogin, IFormFile image)
    {
        try
        {
            AttachmentService.AssertFileTypeIs(image.ContentType, FileType.Image);
            AssertUserLoginIs(userLogin);
        }
        catch (Exception e)
        {
            return BadRequest(e.Message);
        }

        await using var stream = image.OpenReadStream();

        await userService.UploadProfileImage(userLogin, stream);
        return Ok();
    }

    [HttpGet("search")]
    public async Task<ActionResult<UserViewModel>> Search(string query, int limit)
    {
        var userDtos = await userService.SearchAsync(query, limit);
        var viewModels = new List<UserViewModel>();
        foreach (var dto in userDtos)
        {
            viewModels.Add(await userViewModelBuilder.BuildAsync(dto));
        }

        return Ok(viewModels);
    }

    [HttpDelete("{userLogin}/profile_image")]
    [Authorize]
    public async Task<IActionResult> DeleteProfileImage(string userLogin)
    {
        try
        {
            AssertUserLoginIs(userLogin);
        }
        catch (Exception e)
        {
            return BadRequest(e.Message);
        }

        await userService.DeleteUserProfileImage(userLogin);
        return Ok();
    }

    private async Task CreateCookieSession(string login)
    {

        var user = await userService.ReadUserByLoginAsync(login);

        var claims = new List<Claim>
        {
            new("/id", user.Id.ToString()),
            new(ClaimTypes.Name, login),
            new(ClaimTypes.Email, user.Email ?? string.Empty),
        };
        var claimIdentity = new ClaimsIdentity(claims, "Cookies");
        await HttpContext.SignInAsync(CookieAuthenticationDefaults.AuthenticationScheme,
            new ClaimsPrincipal(claimIdentity));
    }
}
