namespace AskMe.WebApi.Models;

public class SubscriptionViewModel
{
    public SubscriptionViewModel()
    {
        Name = string.Empty;
        Description = string.Empty;
    }

    public Guid Id { get; set; }
    public string Name { get; set; }
    public string Description { get; set; }
    public Guid AuthorId { get; set; }
    public uint Price { get; set; }
    public bool IsBought { get; set; }
    public bool IsInherit { get; set; }
}
