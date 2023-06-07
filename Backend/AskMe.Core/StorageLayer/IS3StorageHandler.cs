namespace AskMe.Core.StorageLayer;

public interface IS3StorageHandler
{
    public Task UploadFileAsync(Stream fileStream, string fileKey);
    Task DeleteIfExistsAsync(string fileKey);
    Task<bool> IsExistsAsync(string fileKey);
    string? GetFileUrl(string fileKey);
    Task<string[]> GeFileKeysInDirectoryAsync(string directoryKey);
}
