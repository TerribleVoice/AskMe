using AskMe.Core.Models.Dbo;
using AskMe.Core.StorageLayer;

namespace AskMe.Service.Repositories;

public class UserRepository : IUserRepository
{
    private PostgresDbContext dbContext;

    public UserRepository(PostgresDbContext dbContext)
    {
        this.dbContext = dbContext;
    }

    public UserDbo[] GetAll()
    {
        return dbContext.Users.ToArray();
    }
}
