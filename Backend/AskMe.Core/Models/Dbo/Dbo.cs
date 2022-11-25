using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace AskMe.Core.Models.Dbo;

public abstract class Dbo
{
    [Column("id"), Key, Required]
    public Guid Id { get; set; }
}
