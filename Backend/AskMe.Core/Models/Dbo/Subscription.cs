namespace AskMe.Core.Models.Dbo;

public class Subscription : Dbo
{
    public Subscription()
    {
        Description = string.Empty;
        Name = string.Empty;
    }

    public Guid AuthorId { get; set; }
    public uint Price { get; set; }
    public string Name { get; set; }
    public string Description { get; set; }

    //id родительской подписки. Для этой подписки будут наследоваться все права родительской, + добавляться свои собственные.
    //Другими словами родительская подписка ниже уровнем.
    public Guid? ParentSubscriptionId { get; set; }
}
