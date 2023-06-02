import { deleteSubscription } from "@/services/deleteSubscription";
import { Link, useLocation, useParams } from "react-router-dom";

export const DeleteSubscription = () => {
  const { id } = useParams();
  const { LoginName } = useParams();

  const onDeleteSubscription = async () => {
    try {
      const response = await deleteSubscription(id!);
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
      onClick={onDeleteSubscription}
    >
      Удалить подписку
    </Link>
  );
};
