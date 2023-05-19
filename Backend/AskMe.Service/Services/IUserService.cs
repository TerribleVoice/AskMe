using AskMe.Core.Models;
using AskMe.Service.Models;

namespace AskMe.Service.Services;

public interface IUserService
{
    Task CreateUserAsync(UserCreationForm createDto);
    Task UpdateUserAsync(UserUpdateForm updateDto);
    Task<Result> AuthenticateUserAsync(string email, string password);
    Task<UserDto> ReadUserByLoginAsync(string login);
    Task<UserDto?> FindUserByLoginAsync(string login);
    Task<UserDto[]> GetTopAuthorsAsync(int limit);
    Task UploadProfileImage(string userLogin, Stream imageStream);
    Task<string?> GetUserProfileImageUrl(string userLogin);
    Task DeleteUserProfileImage(string userLogin);
}
