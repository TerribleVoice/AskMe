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

    public User Author { get; set; }
    public Subscription Subscription { get; set; }

}

public static class PostExt
{
    public static void TimeToUtc(this Post post)
    {
        //todo проверить что норм приводит
        post.CreatedAt = post.CreatedAt.ToUniversalTime();
    }

    public static IQueryable<Post> FilterByTime(this IQueryable<Post> query, DateTime? time)
    {
        if (!time.HasValue)
        {
            return query;
        }

        var timeUtc = time.Value.ToUniversalTime();
        return query.Where(x => x.CreatedAt >= timeUtc);
    }
}
