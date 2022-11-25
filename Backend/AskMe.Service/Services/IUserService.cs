using AskMe.Service.Models;

namespace AskMe.Service.Services;

public interface IUserService
{
    IEnumerable<UserCreationDto> GetAll();
}
