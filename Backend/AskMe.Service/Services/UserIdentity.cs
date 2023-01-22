using System.Security.Claims;
using AskMe.Core.Models;
using AskMe.Service.Models;

namespace AskMe.Service.Services;

public class UserIdentity : IUserIdentity
{
    public UserDto CurrentUser { get; private set; }

    public void ChangeUser(ClaimsPrincipal claimsPrincipal)
    {
        CurrentUser = new UserDto
            {
                Id = Guid.Parse(claimsPrincipal.FindFirst("/id")!.Value),
                Email = claimsPrincipal.FindFirst(ClaimTypes.Email)!.Value,
                Login = claimsPrincipal.FindFirst(ClaimTypes.Name)!.Value,
                IsAuthor = claimsPrincipal.FindFirst(ClaimTypes.Role)!.Value == Roles.Author
            };
    }

}
