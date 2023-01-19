namespace AskMe.Service.Models;

public class CreatePostRequest
{
    public string? Content { get; set; }
    public Guid SubscriptionId { get; set; }
    public uint? Price { get; set; }
}
