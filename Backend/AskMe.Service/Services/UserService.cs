using AskMe.Core.Models;
using AskMe.Core.StorageLayer;
using AskMe.Service.Converters;
using AskMe.Service.Models;
using Microsoft.EntityFrameworkCore;

namespace AskMe.Service.Services;

public class UserService : IUserService
{
    private readonly PostgresDbContext dbContext;
    private readonly IUserConverter userConverter;

    public UserService(PostgresDbContext dbContext,
        IUserConverter userConverter)
    {
        this.dbContext = dbContext;
        this.userConverter = userConverter;
    }

    public async Task CreateUserAsync(UserCreationForm creationDto)
    {
        var dbo = userConverter.ToDbo(creationDto);

        await dbContext.AddAsync(dbo);
        await dbContext.SaveChangesAsync();
    }

    public async Task<Result> AuthenticateUserAsync(string login, string password)
    {
        var user = await dbContext.Users.FirstOrDefaultAsync(x=>x.Login == login);
        if (user == null)
        {
            return Result.Fail($"Пользователь с логином {login} не найден");
        }

        return user.Password == password
            ? Result.Ok()
            : Result.Fail("Неверный пароль");
    }

    public async Task<UserDto> ReadUserByLoginAsync(string login)
    {
        var user = await dbContext.Users.FirstOrDefaultAsync(x=>x.Login == login);
        if (user == null)
        {
            throw new Exception($"Пользователь с логином {login} не найден");
        }

        return userConverter.ToDto(user);
    }

    public Task<UserDto[]> GetTopAuthorsAsync()
    {
        throw new NotImplementedException();
    }
}
