using AskMe.Models;
using AskMe.Repository;
using Microsoft.AspNetCore.Mvc;

namespace AskMe.Controllers;

[ApiController]
[Route("[controller]")]
public class UserController : ControllerBase
{
    private readonly ILogger<UserController> _logger;
    private readonly WebApiDbContext dbContext;

    public UserController(ILogger<UserController> logger, WebApiDbContext dbContext)
    {
        this.dbContext = dbContext;
        _logger = logger;
    }

    [HttpGet(Name = "GetUsersList")]
    public IEnumerable<User> GetUsersList()
    {
        var users = dbContext.Users.ToList();
        return users;
    }
}
