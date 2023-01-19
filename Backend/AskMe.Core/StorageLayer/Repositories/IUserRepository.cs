using AskMe.Core.Models;
using AskMe.Core.Models.Dbo;

namespace AskMe.Core.StorageLayer.Repositories;

public interface IUserRepository
{
    Task<Result> CreateAsync(UserDbo dbo);
    Result<UserDbo[]> GetAll();
    Task<Result<string>> GetPasswordAsync(string login);
    Task<Result<UserDbo?>> Find(string login);
}
