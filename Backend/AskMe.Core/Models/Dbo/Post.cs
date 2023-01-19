namespace AskMe.Core.Models.Dbo;

public class Post : Dbo
{
    public Guid AuthorId { get; set; }
    public Guid SubscriptionId { get; set; }
    public string Content { get; set; }
    public DateTime CreatedAt { get; set; }
    public uint? Price { get; set; }
}
