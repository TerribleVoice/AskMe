﻿using AskMe.Core.Models;
using AskMe.Core.Models.Dbo;
using Microsoft.EntityFrameworkCore;

namespace AskMe.Core.StorageLayer.Repositories;

public class UserRepository : IUserRepository
{
    private readonly PostgresDbContext postgresDbContext;

    public UserRepository(PostgresDbContext postgresDbContext)
    {
        this.postgresDbContext = postgresDbContext;
    }

    public async Task<Result> CreateAsync(UserDbo dbo)
    {
        try
        {
            await postgresDbContext.Users.AddAsync(dbo);
            await postgresDbContext.SaveChangesAsync();
            return Result.Ok();
        }
        catch (Exception e)
        {
            return Result.Fail(e.Message);
        }
    }

    public Result<UserDbo[]> GetAll()
    {
        try
        {
            var users = postgresDbContext.Users.ToArray();
            return Result.Ok(users);
        }
        catch (Exception e)
        {
            return Result.Fail<UserDbo[]>(e.Message);
        }
    }

    public async Task<Result<string>> GetPasswordAsync(string login)
    {
        var user = await Find(login);
        return user.Value != null
            ? Result.Ok(user.Value.Password)
            : Result.Fail<string>("User not found");
    }

    public async Task<Result<UserDbo?>> Find(string login)
    {
        try
        {
            var user = await postgresDbContext.Users.FirstOrDefaultAsync(x => x.Login == login);
            return Result.Ok(user);
        }
        catch (Exception e)
        {
            return Result.Fail<UserDbo?>(e.Message);
        }
    }
}