using AskMe.Core.Models.Dbo;
using AskMe.Service.Models;

namespace AskMe.Service.Converters;

public class UserConverter : IUserConverter
{

    public User ToDbo(UserCreationForm creationDto)
    {
        return new User
        {
            Id = Guid.NewGuid(),
            Email = creationDto.Email,
            Login = creationDto.Login,
            Password = creationDto.Password,
            QiwiToken = creationDto.QiwiToken,
            Description = creationDto.Description,
            Links = creationDto.Links
        };
    }

    public UserDto? ToDto(User? user)
    {
        if (user == null)
        {
            return null;
        }

        return new UserDto
        {
            Id = user.Id,
            Email = user.Email,
            Login = user.Login,
            QiwiToken = user.QiwiToken,
            Description = user.Description,
            Links = user.Links
        };
    }
}
