using System.Net;
using System.Text;
using Amazon.S3;
using Amazon.S3.Model;
using Amazon.S3.Transfer;

namespace AskMe.Service.Handlers;

public class S3StorageHandler : IS3StorageHandler
{

    private const string bucketName = "askme-drive";
    private const int defaultUrlExpiringDays = 1; //1 день
    private readonly TransferUtility transferUtility;

    public S3StorageHandler(TransferUtility transferUtility)
    {
        this.transferUtility = transferUtility;
    }

    private IAmazonS3 S3Client => transferUtility.S3Client;

    public async Task UploadFile(Stream fileStream, string fileKey)
    {
        await transferUtility.UploadAsync(fileStream, bucketName, fileKey);
    }

    public async Task DeleteIfExists(string fileKey)
    {
        if (await IsExists(fileKey))
        {
            await S3Client.DeleteObjectAsync(bucketName, fileKey);
        }
    }

    public async Task<bool> IsExists(string fileKey)
    {
        try
        {
            await transferUtility.S3Client.GetObjectMetadataAsync(bucketName, fileKey);
            return true;
        }
        catch (AmazonS3Exception ex)
        {
            if (ex.StatusCode == HttpStatusCode.NotFound)
            {
                return false;
            }
            throw;
        }
    }

    public string? GetFileUrl(string fileKey)
    {
        var request = new GetPreSignedUrlRequest
        {
            BucketName = bucketName,
            Key = fileKey,
            Expires = DateTime.Now.AddDays(defaultUrlExpiringDays),
        };
        var url = S3Client.GetPreSignedURL(request);

        return url;
    }

    public static string CreatePath(params string[] parts)
    {
        var sb = new StringBuilder();
        foreach (var part in parts)
        {
            sb.Append($"{part}/");
        }
        sb.Remove(sb.Length - 1, 1);
        return sb.ToString();
    }
}