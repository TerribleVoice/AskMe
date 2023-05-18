using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace AskMe.Core.Models.Dbo;

[Table("bought_subscriptions")]
public class BoughtSubscription : Dbo
{
    public BoughtSubscription()
    {
    }

    public BoughtSubscription(Guid ownerId, Guid subscriptionId)
    {
        Id = Guid.NewGuid();
        OwnerId = ownerId;
        SubscriptionId = subscriptionId;
    }

    [Column("user_id")]
    [Required]
    public Guid OwnerId { get; set; }

    [Column("subscription_id")]
    [Required]
    public Guid SubscriptionId { get; set; }

    public User Owner { get; set; }
    public Subscription Subscription {get; set; }
}
