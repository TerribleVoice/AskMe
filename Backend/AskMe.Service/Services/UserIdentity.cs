using AskMe.Service.Models;

namespace AskMe.Service.Services;

public class UserIdentity : IUserIdentity
{
    public UserDto CurrentUser { get; }
}
