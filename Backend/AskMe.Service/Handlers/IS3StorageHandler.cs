namespace AskMe.Service.Handlers;

public interface IS3StorageHandler
{
    public Task UploadFile(Stream fileStream, string fileKey);
    Task DeleteIfExists(string fileKey);
    Task<bool> IsExists(string fileKey);
    string? GetFileUrl(string fileKey);
}
