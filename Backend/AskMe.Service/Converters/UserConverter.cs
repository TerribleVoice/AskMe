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
            IsAuthor = creationDto.IsAuthor,
            QiwiToken = creationDto.QiwiToken
        };
    }

    public UserDto ToDto(User user)
    {
        return new UserDto
        {
            IsAuthor = user.IsAuthor,
            Id = user.Id,
            Email = user.Email,
            Login = user.Login,
            QiwiToken = user.QiwiToken
        };
    }
}
