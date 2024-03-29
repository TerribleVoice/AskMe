import { deleteUserPhoto } from "@/services/deleteUserPhoto";
import { Link, useLocation, useNavigate, useParams } from "react-router-dom";

export const UserSettingsDeletePhoto = () => {
  const { LoginName } = useParams();

  const onDeletePhoto = async () => {
    try {
      const response = await deleteUserPhoto(LoginName!);
      console.log(response);
      if (response.status < 300) {
      } else {
        alert("Reject");
      }
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <Link
      to={`/${LoginName}`}
      className="settings_delete_photo"
      onClick={onDeletePhoto}
    >
      Удалить фотографию
    </Link>
  );
};
