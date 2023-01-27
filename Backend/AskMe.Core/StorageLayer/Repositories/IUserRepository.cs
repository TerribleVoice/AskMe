using AskMe.Core.Models;
using AskMe.Core.Models.Dbo;

namespace AskMe.Core.StorageLayer.Repositories;

public interface IUserRepository
{
    Task<Result> CreateAsync(User dbo);
    Result<User[]> GetAll();
    Task<Result<string>> GetPasswordAsync(string login);
    Task<Result<User?>> Find(string login);

    Task<Result<User>> ReadByLogin(string login);
}
