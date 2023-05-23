using AskMe.WebApi.Enums;

namespace AskMe.WebApi.Models;

public class AttachmentRequest
{
    public Stream FileStream { get; set; }
    public string Name { get; set; }
    public FileType Type { get; set; }
}
