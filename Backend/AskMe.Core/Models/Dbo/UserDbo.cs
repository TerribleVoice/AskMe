using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace AskMe.Core.Models.Dbo;

[Table("users")]
public class UserDbo : Dbo
{
    public UserDbo()
    {
    Login = string.Empty;
    Password = string.Empty;
    }

    [Column("login")]
    [Required(AllowEmptyStrings = true)]
    [MaxLength(100)]
    public string Login { get; set; }

    [Column("email")]
    [Required(AllowEmptyStrings = true)]
    [MaxLength(150)]
    public string? Email { get; set; }

    [Column("password")]
    [Required(AllowEmptyStrings = true)]
    [MaxLength(100)]
    public string Password { get; set; }

    [Column("is_author")]
    [Required]
    public bool IsAuthor { get; set; }
}
