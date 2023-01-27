using AskMe.Core.Models;
using AskMe.Core.Models.Dbo;
using AskMe.Core.StorageLayer.Repositories;
using AskMe.Service.Converters;
using AskMe.Service.Models;

namespace AskMe.Service.Services;

public class UserService : IUserService
{
    private readonly IUserRepository userRepository;
    private readonly IUserConverter userConverter;

    public UserService(IUserRepository userRepository, IUserConverter userConverter)
    {
        this.userRepository = userRepository;
        this.userConverter = userConverter;
    }

    public async Task<Result> CreateUser(UserCreationForm creationDto)
    {
        var dbo = userConverter.ToDbo(creationDto);
        return await userRepository.CreateAsync(dbo);
    }

    public async Task<Result> AuthenticateUser(string login, string password)
    {
        var actualPasswordResult = await userRepository.GetPasswordAsync(login);
        if (actualPasswordResult.IsFailure)
        {
            return actualPasswordResult;
        }

        return actualPasswordResult.Value == password
            ? Result.Ok()
            : Result.Fail("Wrong login or password");
    }

    public async Task<Result<UserDto>> FindUserByLogin(string login)
    {
        var userResult = await userRepository.ReadByLogin(login);
        if (userResult.IsFailure)
        {
            return Result.Fail<UserDto, User>(userResult);
        }
        return Result.Ok(userConverter.ToDto(userResult.Value!));
    }

    public Result<IEnumerable<UserDto>> GetAll()
    {
        var dbos = userRepository.GetAll();
        return Result.Ok(dbos.Value!.Select(x => new UserDto { Id = x.Id }));
    }
}
