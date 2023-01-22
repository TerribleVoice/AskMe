using AskMe.Core.Models;
using AskMe.Service.Models;

namespace AskMe.Service.Services;

public interface IUserService
{
    Result<IEnumerable<UserDto>> GetAll();
    Task<Result> CreateUser(UserCreationForm creationDto);
    Task<Result> AuthenticateUser(string email, string password);
    Task<Result<UserDto>> FindUserByLogin(string login);
}
