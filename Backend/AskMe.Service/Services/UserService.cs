using AskMe.Service.Models;
using AskMe.Service.Repositories;

namespace AskMe.Service.Services;

public class UserService : IUserService
{
    private readonly IUserRepository userRepository;

    public UserService(IUserRepository userRepository)
    {
        this.userRepository = userRepository;
    }

    public Task CreateUser(UserCreationDto creationDto)
    {
        
    }

    public IEnumerable<UserCreationDto> GetAll()
    {
        var dbos = userRepository.GetAll();
        return dbos.Select(x => new UserCreationDto { Id = x.Id });
    }
}
