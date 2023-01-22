using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace AskMe.Core.Models.Dbo;

[Table("posts")]
public class Post : Dbo
{
    public Post()
    {
        Content = string.Empty;
    }

    [Column("author_id")]
    [Required]
    public Guid AuthorId { get; set; }

    [Column("subscription_id")]
    [Required]
    public Guid SubscriptionId { get; set; }

    [Column("content")]
    [Required(AllowEmptyStrings = false)]
    public string Content { get; set; }

    [Column("created_at")]
    [Required]
    public DateTime CreatedAt { get; set; }

    [Column("price")]
    public uint? Price { get; set; }

}
