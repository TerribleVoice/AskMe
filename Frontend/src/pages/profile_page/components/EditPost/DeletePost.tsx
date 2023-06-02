import { deleteUserPost } from "@/services/deleteUserPost";
import { Link, useLocation, useNavigate, useParams } from "react-router-dom";

export const DeletePost = () => {
  const { id } = useParams();
  const { LoginName } = useParams();

  const onDeletePost = async () => {
    try {
      const response = await deleteUserPost(id!);
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
      className="settings_delete_sub"
      onClick={onDeletePost}
    >
      Удалить пост
    </Link>
  );
};
