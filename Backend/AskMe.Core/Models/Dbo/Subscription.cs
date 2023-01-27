using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace AskMe.Core.Models.Dbo;

public class Subscription : Dbo
{
    public Subscription()
    {
        Description = string.Empty;
        Name = string.Empty;
    }
    [Column("author_id")]
    [Required]
    public Guid AuthorId { get; set; }

    [Column("price")]
    [Required]
    public uint Price { get; set; }

    [Column("name")]
    [Required(AllowEmptyStrings = false)]
    [MaxLength(100)]
    public string Name { get; set; }

    [Column("description")]
    [Required(AllowEmptyStrings = false)]
    [MaxLength(300)]
    public string Description { get; set; }

    //id родительской подписки. Для этой подписки будут наследоваться все права родительской, + добавляться свои собственные.
    //Другими словами родительская подписка ниже уровнем.
    [Column("parent_subscription_id")]
    public Guid? ParentSubscriptionId { get; set; }
}
