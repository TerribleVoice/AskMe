namespace AskMe.Service.Models;

public class PostResponse
{
    public PostResponse()
    {
        Content = string.Empty;
    }

    public Guid Id { get; set; }
    public string Content { get; set; }
    public uint? Price { get; set; }
    public DateTime CreateAt { get; set; }
    public Guid SubscriptionId { get; set; }
}
