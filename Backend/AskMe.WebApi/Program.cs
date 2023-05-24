using Amazon;
using Amazon.S3;
using Amazon.S3.Transfer;
using AskMe.Core.Models;
using AskMe.Core.StorageLayer;
using AskMe.Service.Converters;
using AskMe.Service.Services;
using AskMe.WebApi.Builders;
using Microsoft.AspNetCore.Authentication.Cookies;
using Microsoft.EntityFrameworkCore;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.

builder.Services.AddControllers();
// Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();
builder.Services.AddHttpContextAccessor();
builder.Services.AddCors();

builder.Services.AddScoped<IUserService, UserService>();
builder.Services.AddScoped<IUserConverter, UserConverter>();

builder.Services.AddScoped<IFeedService, FeedService>();
builder.Services.AddScoped<IPostConverter, PostConverter>();

builder.Services.AddScoped<ISubscriptionService, SubscriptionService>();
builder.Services.AddScoped<ISubscriptionConverter, SubscriptionConverter>();

builder.Services.AddScoped<UserViewModelBuilder>();
builder.Services.AddScoped<PostViewModelBuilder>();

AddUserIdentity(builder);

builder.Services.AddDbContext<PostgresDbContext>(optionsBuilder =>
{
    var dbConnectionString = builder.Configuration.GetConnectionString("WebApi");
    optionsBuilder.UseNpgsql(dbConnectionString);
});

AddS3StorageHandler(builder);

builder.Services.AddAuthentication(CookieAuthenticationDefaults.AuthenticationScheme).AddCookie();
builder.Services.AddAuthorization();

var app = builder.Build();


app.UseAuthentication();
app.UseAuthorization();
// Configure the HTTP request pipeline.
if (app.Environment.IsEnvironment("docker")|| app.Environment.IsEnvironment("local"))
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseCors(corsBuilder => corsBuilder
    .AllowAnyHeader()
    .AllowAnyMethod()
    .SetIsOriginAllowed(_ => true)
    .AllowCredentials()
);

app.MapControllers();
app.Run();




void AddUserIdentity(WebApplicationBuilder webApplicationBuilder)
{
    webApplicationBuilder.Services.AddScoped<IUserIdentity, UserIdentity>(sp =>
    {
        var httpContextAccessor = sp.GetService<IHttpContextAccessor>();
        if (httpContextAccessor == null ||
            httpContextAccessor.HttpContext?.User.Identity?.IsAuthenticated is false)
        {
            return new UserIdentity();
        }
        var claimsPrincipal = httpContextAccessor.HttpContext!.Request.HttpContext.User;
        var identity = new UserIdentity(claimsPrincipal);
        return identity;
    });
}

void AddS3StorageHandler(WebApplicationBuilder builder1)
{
    builder1.Services.AddSingleton<IS3StorageHandler, S3StorageHandler>(_ =>
    {
        var amazonS3Config = new AmazonS3Config
        {
            RegionEndpoint = RegionEndpoint.USEast1,
            ServiceURL = "https://s3.yandexcloud.net"
        };
        var s3Client = new AmazonS3Client("YCAJEOvh1uMB1fiQ_3jOziPuU",
            "YCPsl1Nvdu-h9YpS-eBQuX0zGcZcvOYhTgLs1GXa",
            amazonS3Config);
        var transferUtility = new TransferUtility(s3Client);

        return new S3StorageHandler(transferUtility);
    });
}
