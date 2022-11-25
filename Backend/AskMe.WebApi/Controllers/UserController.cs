using AskMe.Service.Models;
using AskMe.Service.Services;
using Microsoft.AspNetCore.Mvc;

namespace AskMe.Controllers;

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
    public IEnumerable<UserCreationDto> GetUsersList()
    {
        var users = userService.GetAll();
        return users;
    }
}
