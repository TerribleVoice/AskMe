namespace AskMe.Service.Models;

public class PostRequest
{
    public string? Content { get; set; }
    public Guid SubscriptionId { get; set; }
    public string Title { get; set; }
}
