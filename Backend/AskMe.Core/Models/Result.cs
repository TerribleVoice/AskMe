namespace AskMe.Core.Models;

public class Result
{
    private Result(bool isSuccess, string? msg = null)
    {
        IsSuccess = isSuccess;
        ErrorMsg = msg;
    }

    public bool IsSuccess { get; set; }
    public bool IsFailure => !IsSuccess;
    public string? ErrorMsg { get; set; }

    public static Result Ok() => new(true);
    public static Result Fail(string msg) => new(false, msg);
}

public class Result<T>
{
    public T? Value { get; set; }
    public bool IsSuccess { get; set; }
    public bool IsFailure => !IsSuccess;
    public string? ErrorMsg { get; set; }
    private Result(bool isSuccess, T? value, string? msg = null)
    {
        Value = value;
        IsSuccess = isSuccess;
        ErrorMsg = msg;
    }

    public static Result<T> Ok(T value) => new(true, value);
    public static Result<T> Fail(string msg) => new(false, default, msg);
}
