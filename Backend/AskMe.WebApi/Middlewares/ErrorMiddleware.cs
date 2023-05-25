using System.Net;
using Newtonsoft.Json;

namespace AskMe.WebApi.Middlewares;

public class ErrorMiddleware
{
    private readonly RequestDelegate next;

    public ErrorMiddleware(RequestDelegate next)
    {
        this.next = next;
    }

    public async Task Invoke(HttpContext context)
    {
        try
        {
            await next(context);
        }
        catch (Exception? ex)
        {
            await HandleExceptionAsync(context, ex);
        }
    }

    private static async Task HandleExceptionAsync(HttpContext context, Exception? exception)
    {
        if (exception == null)
            return;

        var code = HttpStatusCode.InternalServerError;

        //wite is proper for Web API, but here you can do what you want
        await WriteExceptionAsync(context, exception, code).ConfigureAwait(false);
    }

    private static async Task WriteExceptionAsync(HttpContext context, Exception exception, HttpStatusCode code)
    {
        var response = context.Response;
        response.ContentType = "application/json";
        response.StatusCode = (int)code;
        await response.WriteAsync(JsonConvert.SerializeObject(new
        {
            error = new
            {
                message = exception.Message,
                exception = exception.GetType().Name
            }
        })).ConfigureAwait(false);
    }
}
