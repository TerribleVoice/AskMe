using AskMe.WebApi.Enums;

namespace AskMe.Service.Models;

public class AttachmentResponse
{
    public AttachmentResponse()
    {
        SourceUrl = string.Empty;
    }

    public FileType FileType { get; set; }
    public string? SourceUrl { get; set; }
}
