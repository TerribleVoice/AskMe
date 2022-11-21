using AskMe.Models;
using Microsoft.EntityFrameworkCore;

namespace AskMe.Repository;

public class WebApiDbContext : DbContext
{
    public WebApiDbContext(DbContextOptions dbContextOptions) : base(dbContextOptions)
    {

    }

    public DbSet<User> Users { get; set; }
}
