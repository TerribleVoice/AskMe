using System.Security.Claims;
using AskMe.Core.Models.Dbo;

namespace AskMe.Core.Models;

public class UserIdentity : IUserIdentity
{
    public UserIdentity()
    {
        CurrentUser = null;
    }

    public UserIdentity(ClaimsPrincipal claimsPrincipal)
    {
        CurrentUser = new User
        {
            Id = Guid.Parse(claimsPrincipal.FindFirst("/id")!.Value),
            Email = claimsPrincipal.FindFirst(ClaimTypes.Email)!.Value,
            Login = claimsPrincipal.FindFirst(ClaimTypes.Name)!.Value,
        };
    }

    public User? CurrentUser { get; }
}
