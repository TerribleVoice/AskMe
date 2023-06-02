import { deleteUserPost } from "@/services/deleteUserPost";
import { Link, useLocation, useParams } from "react-router-dom";

export const DeletePost = () => {
  const { id } = useParams();
  const location = useLocation()

  const onDeletePost = async () => {
    try {
      const response = await deleteUserPost(id!);
      console.log(response);
      if (response.status < 300) {
        alert("Confirm");
      } else {
        alert("Reject");
      }
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <Link
      to={location.pathname}
      className="settings_delete_sub"
      onClick={onDeletePost}
    >
      Удалить пост
    </Link>
  );
};
