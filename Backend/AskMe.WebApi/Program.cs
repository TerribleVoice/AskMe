
using System.Security.Claims;
using AskMe.Core.Models;
using AskMe.Core.StorageLayer;
using AskMe.Core.StorageLayer.Repositories;
using AskMe.Service.Converters;
using AskMe.Service.Services;
using Microsoft.AspNetCore.Authentication.Cookies;
using Microsoft.EntityFrameworkCore;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.

builder.Services.AddControllers();
// Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

builder.Services.AddScoped<IUserService, UserService>();
builder.Services.AddScoped<IUserRepository, UserRepository>();
builder.Services.AddScoped<IUserConverter, UserConverter>();

builder.Services.AddScoped<IFeedService, FeedService>();
builder.Services.AddScoped<IPostRepository, PostRepository>();
builder.Services.AddScoped<IPostConverter, PostConverter>();

builder.Services.AddScoped<IUserIdentity>(sp =>
{
    var httpContextAccessor = sp.GetService<IHttpContextAccessor>();
    if (httpContextAccessor == null || httpContextAccessor.HttpContext?.User.Identity?.IsAuthenticated != null
        && !httpContextAccessor.HttpContext.User.Identity.IsAuthenticated)
    {
        return new UserIdentity();
    }
    var identity = httpContextAccessor.HttpContext!.User;
    return new UserIdentity
    {
        CurrentUser =
        {
            Id = Guid.Parse(identity.FindFirst("/id")!.Value),
            Email = identity.FindFirst(ClaimTypes.Email)!.Value,
            Login = identity.FindFirst(ClaimTypes.Name)!.Value,
            IsAuthor = identity.FindFirst(ClaimTypes.Role)!.Value == Roles.Author
        }
    };
});

builder.Services.AddDbContext<PostgresDbContext>(optionsBuilder =>
{
    var dbConnectionString = builder.Configuration.GetConnectionString("WebApi");
    optionsBuilder.UseNpgsql(dbConnectionString);
});

builder.Services.AddAuthentication(CookieAuthenticationDefaults.AuthenticationScheme)
    .AddCookie();
builder.Services.AddAuthorization();

var app = builder.Build();

app.UseAuthentication();
app.UseAuthorization();
// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseHttpsRedirection();

app.MapControllers();

app.Run();
