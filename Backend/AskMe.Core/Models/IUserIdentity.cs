using AskMe.Core.Models.Dbo;

namespace AskMe.Core.Models;

public interface IUserIdentity
{
    User? CurrentUser { get; }
}
