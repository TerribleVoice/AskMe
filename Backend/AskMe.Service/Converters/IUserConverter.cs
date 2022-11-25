using AskMe.Core.Models.Dbo;
using AskMe.Service.Models;

namespace AskMe.Service.Converters;

public interface IUserConverter
{
    public UserDbo ToDbo(UserCreationDto creationDto);
}
