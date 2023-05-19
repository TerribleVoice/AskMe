using System.ComponentModel.DataAnnotations;
using AskMe.Core.Models;
using AskMe.Core.Models.Dbo;
using AskMe.WebApi.Enums;
using Microsoft.AspNetCore.Mvc;

namespace AskMe.WebApi.Controllers;

public class CustomControllerBase : ControllerBase
{
    private readonly IUserIdentity userIdentity;

    public CustomControllerBase(IUserIdentity userIdentity)
    {
        this.userIdentity = userIdentity;
    }

    protected User? CurrentUser => userIdentity.CurrentUser;

    protected IActionResult ProcessResult(Result operationResult)
    {
        if (operationResult.IsFailure)
        {
            return BadRequest(operationResult.ErrorMsg);
        }

        return Ok();
    }

    protected void AssertFileTypeIs(IFormFile file, FileType type)
    {
        switch (type)
        {
            case FileType.Image:
                if (!file.ContentType.StartsWith("image"))
                {
                    throw new ArgumentException($"Файл {file.FileName} не является изображением");
                }
                break;
            case FileType.Video:
                if (!file.ContentType.StartsWith("video"))
                {
                    throw new ArgumentException($"Файл {file.FileName} не является видео");
                }
                break;
            case FileType.Text:
                if (!file.ContentType.StartsWith("text"))
                {
                    throw new ArgumentException($"Файл {file.FileName} не является текстом");
                }
                break;
            case FileType.Audio:
                if (!file.ContentType.StartsWith("audio"))
                {
                    throw new ArgumentException($"Файл {file.FileName} не является аудио");
                }
                break;
            default:
                throw new ArgumentOutOfRangeException(nameof(type), type, "Незвестный тип");
        }
    }

    protected void AssertUserLoginIs(string login)
    {
        if (CurrentUser == null || CurrentUser.Login != login)
        {
            throw new ValidationException($"Пользователь {CurrentUser?.Login} это не {login}");
        }
    }
}
