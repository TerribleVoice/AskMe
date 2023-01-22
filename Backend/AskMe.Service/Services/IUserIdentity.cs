using System.Security.Claims;
using AskMe.Service.Models;

namespace AskMe.Service.Services;

public interface IUserIdentity
{
    UserDto CurrentUser { get; }
    void ChangeUser(ClaimsPrincipal claimsPrincipal);
}
