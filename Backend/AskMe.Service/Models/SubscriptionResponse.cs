namespace AskMe.Service.Models;

public class SubscriptionResponse
{
    public SubscriptionResponse()
    {
        Description = string.Empty;
        Name = string.Empty;
    }

    public Guid Id { set; get; }
    public Guid AuthorId { get; set; }
    public uint Price { get; set; }
    public string Name { get; set; }
    public string Description { get; set; }
    public Guid? ParentSubscriptionId { get; set; }
}
