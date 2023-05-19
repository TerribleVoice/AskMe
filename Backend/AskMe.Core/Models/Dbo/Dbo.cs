using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Reflection;

namespace AskMe.Core.Models.Dbo;

public abstract class Dbo
{
    [Column("id"), Key, Required]
    public Guid Id { get; set; }
}

public static class DboExtensions
{
    public static void UpdateByDbo<T>(this T dbo, T anotherDbo) where T: Dbo
    {
        var properties = typeof(T).GetProperties(BindingFlags.Public | BindingFlags.Instance);

        foreach (var property in properties)
        {
            if (property.GetCustomAttribute<ColumnAttribute>() != null && property.Name != "Id")
            {
                var value = property.GetValue(anotherDbo);
                property.SetValue(dbo, value);
            }
        }
    }
}
