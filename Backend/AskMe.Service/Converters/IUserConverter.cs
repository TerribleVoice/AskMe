using AskMe.Core.Models.Dbo;
using AskMe.Service.Models;
using AskMe.WebApi.Models;

namespace AskMe.Service.Converters;

public interface IUserConverter
{
    public UserDbo ToDbo(UserCreationForm creationDto);
    public UserDto ToDto(UserDbo user);
}
