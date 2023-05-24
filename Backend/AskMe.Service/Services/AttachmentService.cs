using AskMe.WebApi.Enums;

namespace AskMe.Service.Services;

public class AttachmentService
{
    public static void AssertFileTypeIs(string contentType, FileType type)
    {
        switch (type)
        {
            case FileType.Image:
                if (!contentType.StartsWith("image"))
                {
                    throw new ArgumentException("Файл не является изображением");
                }
                break;
            case FileType.Video:
                if (!contentType.StartsWith("video"))
                {
                    throw new ArgumentException("Файл не является видео");
                }
                break;
            case FileType.Text:
                if (!contentType.StartsWith("text"))
                {
                    throw new ArgumentException("Файл не является текстом");
                }
                break;
            case FileType.Audio:
                if (!contentType.StartsWith("audio"))
                {
                    throw new ArgumentException("Файл не является аудио");
                }
                break;
            default:
                throw new ArgumentOutOfRangeException(nameof(type), type, "Незвестный тип");
        }
    }

    public static FileType GetFileType(string contentType)
    {
        if (contentType.StartsWith("image"))
        {
            return FileType.Image;
        }
        if (contentType.StartsWith("video"))
        {
            return FileType.Video;
        }
        if (contentType.StartsWith("audio"))
        {
            return FileType.Audio;
        }
        if (contentType.StartsWith("text"))
        {
            return FileType.Text;
        }
        throw new ArgumentOutOfRangeException($"Неподдерживаемый тип {contentType}");
    }
}
