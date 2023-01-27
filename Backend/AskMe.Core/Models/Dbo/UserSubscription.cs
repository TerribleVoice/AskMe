using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace AskMe.Core.Models.Dbo;

public class UserSubscription : Dbo
{
    public UserSubscription()
    {
    }

    public UserSubscription(Guid userId, Guid subscriptionId)
    {
        Id = Guid.NewGuid();
        UserId = userId;
        SubscriptionId = subscriptionId;
    }

    [Column("user_id")]
    [Required]
    public Guid UserId { get; set; }

    [Column("user_id")]
    [Required]
    public Guid SubscriptionId { get; set; }
}
