import { deleteSubscription } from "@/services/deleteSubscription";
import { Link, useLocation, useParams } from "react-router-dom";

export const DeleteSubscription = () => {
  const { id } = useParams();
  const location = useLocation()

  const onDeleteSubscription = async () => {
    try {
      const response = await deleteSubscription(id!);
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
      onClick={onDeleteSubscription}
    >
      Удалить подписку
    </Link>
  );
};
