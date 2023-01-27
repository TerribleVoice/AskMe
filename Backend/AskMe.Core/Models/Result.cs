namespace AskMe.Core.Models;

public class Result
{
    protected Result(bool isSuccess, string? msg = null)
    {
        IsSuccess = isSuccess;
        ErrorMsg = msg;
    }

    public bool IsSuccess { get; set; }
    public bool IsFailure => !IsSuccess;
    public string? ErrorMsg { get; set; }

    public static Result Ok() => new(true);
    public static Result Fail(string msg) => new(false, msg);
    public static Result<T> Ok<T>(T value) => new(true, value);
    public static Result<T> Fail<T>(string msg) => new(false, default, msg);
    public static Result From<T>(Result<T> rootResult) => new(rootResult.IsSuccess, rootResult.ErrorMsg);
    public static Result<T1> Fail<T1, T2>(Result<T2> rootResult) => new(false, default, rootResult.ErrorMsg);

    public Result ThrowIfFailure()
    {
        if (IsFailure)
        {
            throw new ArgumentException(ErrorMsg);
        }

        return this;
    }

}

public class Result<T> : Result
{
    public T? Value { get; set; }

    protected internal Result(bool isSuccess, T? value, string? msg = null) : base(isSuccess, msg)
    {
        Value = value;
    }
    public new T ThrowIfFailure()
    {
        if (IsFailure)
        {
            throw new ArgumentException(ErrorMsg);
        }

        return Value!;
    }
}
