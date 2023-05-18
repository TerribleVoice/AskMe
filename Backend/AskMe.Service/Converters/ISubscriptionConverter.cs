using AskMe.Core.Models.Dbo;
using AskMe.Service.Models;

namespace AskMe.Service.Converters;

public interface ISubscriptionConverter
{
    SubscriptionResponse Convert(Subscription subscription);
    Subscription Convert(Guid subscriptionId, Guid authorId, SubscriptionRequest request);
    Subscription Convert(SubscriptionResponse subscriptionResponse);
}
