using AskMe.Core.Models.Dbo;

namespace AskMe.Service.Repositories;

public interface IUserRepository
{
    UserDbo[] GetAll();
}
