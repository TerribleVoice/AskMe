using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace AskMe.Core.Models.Dbo;

[Table("users")]
public class User : Dbo
{
    public User()
    {
        Login = string.Empty;
        Password = string.Empty;
    }

    [Column("login")]
    [Required(AllowEmptyStrings = false)]
    [MaxLength(100)]
    public string Login { get; set; }

    [Column("email")]
    [Required(AllowEmptyStrings = false)]
    [MaxLength(150)]
    public string? Email { get; set; }

    [Column("password")]
    [Required(AllowEmptyStrings = false)]
    [MaxLength(100)]
    public string Password { get; set; }

    [Column("is_author")]
    [Required]
    public bool IsAuthor { get; set; }

    [Column("qiwi_token")]
    [MaxLength(200)]
    public string? QiwiToken { get; set; }

    [Column("description")]
    public string? Description { get; set; }

    [Column("description")]
    public string? Links { get; set; }
}
