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
    private readonly IS3StorageHandler s3StorageHandler;

    public UserService(PostgresDbContext dbContext,
        IUserConverter userConverter,
        IS3StorageHandler s3StorageHandler)
    {
        this.dbContext = dbContext;
        this.userConverter = userConverter;
        this.s3StorageHandler = s3StorageHandler;
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
                x.BoughtSubscriptions.Count
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

    public async Task<UserDto[]> SearchAsync(string query, int limit)
    {
        var innerQuery = query.Trim();
        var startsWith = await dbContext.Users
            .Where(x => x.Login.StartsWith(innerQuery, StringComparison.InvariantCultureIgnoreCase))
            .ToArrayAsync();
        var result = startsWith;
        if (startsWith.Length < limit)
        {
            var contains = await dbContext.Users.Where(x => x.Login.Contains(innerQuery)).ToArrayAsync();
            result = startsWith.UnionBy(contains, x => x.Id).ToArray();
        }

        return result.Select(userConverter.ToDto).ToArray()!;
    }

    public async Task UploadProfileImage(string userLogin, Stream imageStream)
    {
        var user = await ReadUserByLoginAsync(userLogin);
        var path = CreateFilePathForProfileImage(user.Id);

        await s3StorageHandler.DeleteIfExists(path);
        await s3StorageHandler.UploadFileAsync(imageStream, path);
    }

    public async Task<string> GetUserProfileImageUrl(string userLogin)
    {
        var user = await ReadUserByLoginAsync(userLogin);
        var path = CreateFilePathForProfileImage(user.Id);
        if (await s3StorageHandler.IsExists(path))
        {
            return s3StorageHandler.GetFileUrl(path);
        }
        return null;
    }

    public async Task DeleteUserProfileImage(string userLogin)
    {
        var user = await ReadUserByLoginAsync(userLogin);
        var path = CreateFilePathForProfileImage(user.Id);

        await s3StorageHandler.DeleteIfExists(path);
    }

    private static string CreateFilePathForProfileImage(Guid userId)
    {
        return S3StorageHandler.CreatePath("userProfileImages", userId.ToString("D"), "avatar");
    }
}
