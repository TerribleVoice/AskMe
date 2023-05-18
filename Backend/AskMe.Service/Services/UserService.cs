using AskMe.Core.Models;
using AskMe.Core.Models.Dbo;
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

    public async Task CreateUserAsync(UserCreationForm createDto)
    {
        var dbo = userConverter.ToDbo(createDto);

        await dbContext.AddAsync(dbo);
        await dbContext.SaveChangesAsync();
    }

    public async Task UpdateUserAsync(UserUpdateForm updateDto)
    {
        var user = await dbContext.Users.SingleAsync(x=>x.Login == updateDto.OldLogin);
        var dbo = userConverter.ToDbo(updateDto);
        user.UpdateByDbo(dbo);

        dbContext.Users.Update(user);
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
        var user = await FindUserByLoginAsync(login);
        if (user == null)
        {
            throw new Exception($"Пользователь с логином {login} не найден");
        }

        return user;
    }

    public async Task<UserDto?> FindUserByLoginAsync(string login)
    {
        var user = await dbContext.Users.FirstOrDefaultAsync(x=>x.Login == login);

        return userConverter.ToDto(user);
    }

    public async Task<UserDto[]> GetTopAuthorsAsync(int limit)
    {
        var readersBySubscription = await dbContext.Subscription
            .Select(x => new
            {
                x.AuthorId,
                Count = x.BoughtSubscriptions.DistinctBy(y => y.OwnerId).Count()
            })
            .ToArrayAsync();

        var authorIds = readersBySubscription.GroupBy(x => x.AuthorId)
            .Select(x => new { AuthorId = x.Key, Count = x.Sum(y => y.Count) })
            .OrderByDescending(x => x.Count)
            .Select(x=>x.AuthorId)
            .Take(limit)
            .ToArray();

        var users = await dbContext.Users.Where(x => authorIds.Contains(x.Id)).ToArrayAsync();
        return users.Select(userConverter.ToDto).ToArray()!;
    }
}
