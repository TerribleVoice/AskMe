﻿using AskMe.Core.Models;
using AskMe.Core.Models.Dbo;
using Microsoft.EntityFrameworkCore;

namespace AskMe.Core.StorageLayer;

public class PostgresDbContext : DbContext
{
    private readonly IUserIdentity userIdentity;
    private readonly EntityState[] modifiedTypes = { EntityState.Added, EntityState.Deleted, EntityState.Modified };

    public PostgresDbContext(DbContextOptions dbContextOptions, IUserIdentity userIdentity) : base(dbContextOptions)
    {
        this.userIdentity = userIdentity;
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

    public async Task SaveChangesAsync()
    {
        var entries = ChangeTracker.Entries();
        foreach (var entry in entries)
        {
            if (entry.Entity is IHaveAuthor && entry.Entity is Dbo && modifiedTypes.Contains(entry.State))
            {
                var entity = (IHaveAuthor)entry.Entity;
                var dbo = (Dbo)entry.Entity;
                if (userIdentity.CurrentUser == null || entity.AuthorId != userIdentity.CurrentUser.Id)
                {
                    throw new Exception($"Недостаточно прав для редактирования объекта {entry.Entity.GetType().Name} " +
                                        $"c id {dbo.Id} у пользователя {userIdentity.CurrentUser?.Login}");
                }
            }
        }
        await base.SaveChangesAsync();
    }

    public async Task<bool> CanUserEdit<T>(Guid entityId, Guid userId) where T : Dbo, IHaveAuthor
    {
        var entityAuthorId = await Set<T>().Where(x => x.Id == entityId).Select(x => x.AuthorId).FirstAsync();
        return entityAuthorId == userId;
    }

    public async Task<bool> CanCurrentUserEdit<T>(Guid entityId) where T : Dbo, IHaveAuthor
    {
        if (userIdentity.CurrentUser == null)
        {
            throw new Exception("Пользователь не авторизован");
        }

        return await CanUserEdit<T>(entityId, userIdentity.CurrentUser!.Id);
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
