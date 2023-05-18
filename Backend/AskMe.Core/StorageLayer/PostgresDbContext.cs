using Microsoft.EntityFrameworkCore;
using AskMe.Core.Models.Dbo;

namespace AskMe.Core.StorageLayer;

public class PostgresDbContext : DbContext
{
    public PostgresDbContext(DbContextOptions dbContextOptions) : base(dbContextOptions)
    {
    }

    public DbSet<User> Users { get; set; }
    public DbSet<Post> Posts { get; set; }
    public DbSet<Subscription> Subscription { get; set; }
    public DbSet<BoughtSubscription> BoughtSubscriptions { get; set; }

    public async Task<T> ReadAsync<T>(Guid entityId) where T:Dbo
    {
        var entity = await Set<T>().FirstOrDefaultAsync(x=>x.Id == entityId);
        if (entity == null)
        {
            throw new Exception($"{nameof(T)} c id {entityId} не найден");
        }
        return entity;
    }

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        base.OnModelCreating(modelBuilder);

        modelBuilder.Entity<User>(entity =>
        {
            entity.HasMany(x => x.Posts)
                .WithOne(x => x.Author)
                .HasForeignKey(x => x.AuthorId);

            entity.HasMany(x => x.BoughtSubscriptions)
                .WithOne(x => x.Owner)
                .HasForeignKey(x => x.OwnerId);

            entity.HasMany(x => x.CreatedSubscriptions)
                .WithOne(x => x.Author)
                .HasForeignKey(x => x.AuthorId);
        });

        modelBuilder.Entity<Post>(entity =>
        {
            entity.HasOne(x => x.Author)
                .WithMany(x => x.Posts)
                .HasForeignKey(x => x.AuthorId)
                .IsRequired();

            entity.HasOne(x => x.Subscription)
                .WithMany(x => x.Posts)
                .HasForeignKey(x => x.SubscriptionId)
                .IsRequired();
        });

        modelBuilder.Entity<Subscription>(entity =>
        {
            entity.HasOne(x => x.Author)
                .WithMany(x => x.CreatedSubscriptions)
                .HasForeignKey(x => x.AuthorId)
                .IsRequired();

            entity.HasMany(x => x.BoughtSubscriptions)
                .WithOne(x => x.Subscription)
                .HasForeignKey(x => x.SubscriptionId);

            entity.HasMany(x => x.Posts)
                .WithOne(x => x.Subscription)
                .HasForeignKey(x => x.SubscriptionId);
        });

        modelBuilder.Entity<BoughtSubscription>(entity =>
        {
            entity.HasOne(x => x.Subscription)
                .WithMany(x => x.BoughtSubscriptions)
                .HasForeignKey(x => x.SubscriptionId)
                .IsRequired();

            entity.HasOne(x => x.Owner)
                .WithMany(x => x.BoughtSubscriptions)
                .HasForeignKey(x => x.OwnerId)
                .IsRequired();
        });


    }
}
