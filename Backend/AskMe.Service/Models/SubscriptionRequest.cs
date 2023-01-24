namespace AskMe.Service.Models;

public class SubscriptionRequest
{
    public SubscriptionRequest()
    {
        Description = string.Empty;
        Name = string.Empty;
    }

    public uint Price { get; set; }
    public string Name { get; set; }
    public string Description { get; set; }
    public Guid? ParentSubscriptionId { get; set; }
}
