﻿using AskMe.Core.Models.Dbo;
using Microsoft.EntityFrameworkCore;

namespace AskMe.Core.StorageLayer;

public class PostgresDbContext : DbContext
{
    public PostgresDbContext(DbContextOptions dbContextOptions) : base(dbContextOptions)
    {

    }

    public DbSet<User> Users { get; set; }
    public DbSet<Post> Posts { get; set; }
    public DbSet<Subscription> Subscription { get; set; }
    public DbSet<UserSubscription> UserSubscription { get; set; }
}
