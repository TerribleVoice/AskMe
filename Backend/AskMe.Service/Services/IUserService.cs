using AskMe.Core.Models;
using AskMe.Service.Models;

namespace AskMe.Service.Services;

public interface IUserService
{
    Task CreateUserAsync(UserCreationForm creationDto);
    Task<Result> AuthenticateUserAsync(string email, string password);
    Task<UserDto> ReadUserByLoginAsync(string login);
    Task<UserDto[]> GetTopAuthorsAsync();
    Task<UserDto?> FindUserByLoginAsync(string login);
}
