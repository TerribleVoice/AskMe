using AskMe.Core.Models.Dbo;
using AskMe.Service.Models;

namespace AskMe.Service.Converters;

public class SubscriptionConverter : ISubscriptionConverter
{
    public SubscriptionResponse Convert(Subscription subscription)
    {
        return new SubscriptionResponse
        {
            Id = subscription.Id,
            AuthorId = subscription.AuthorId,
            Price = subscription.Price,
            Name = subscription.Name,
            Description = subscription.Description,
            ParentSubscriptionId = subscription.ParentSubscriptionId
        };
    }

    public Subscription Convert(Guid subscriptionId, Guid authorId, SubscriptionRequest request)
    {
        return new Subscription
        {
            Id = subscriptionId,
            AuthorId = authorId,
            Price = request.Price,
            Name = request.Name,
            Description = request.Description,
            ParentSubscriptionId = request.ParentSubscriptionId
        };
    }

    public Subscription Convert(SubscriptionResponse subscriptionResponse)
    {
        return new Subscription
        {
            Id = subscriptionResponse.Id,
            AuthorId = subscriptionResponse.AuthorId,
            Price = subscriptionResponse.Price,
            Name = subscriptionResponse.Name,
            Description = subscriptionResponse.Description,
            ParentSubscriptionId = subscriptionResponse.ParentSubscriptionId
        };
    }
}
