namespace AskMe.Service.Models;

public class UserUpdateForm : UserCreationForm
{
    public UserUpdateForm()
    {
        OldLogin = string.Empty;
    }

    public string OldLogin { get; set; }
}
