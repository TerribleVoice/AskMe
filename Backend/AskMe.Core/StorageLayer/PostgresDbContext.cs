using AskMe.Core.Models.Dbo;
using Microsoft.EntityFrameworkCore;

namespace AskMe.Core.StorageLayer;

public class PostgresDbContext : DbContext
{
    public PostgresDbContext(DbContextOptions dbContextOptions) : base(dbContextOptions)
    {

    }

    public DbSet<UserDbo> Users { get; set; }
    public DbSet<Post> Posts { get; set; }
}
