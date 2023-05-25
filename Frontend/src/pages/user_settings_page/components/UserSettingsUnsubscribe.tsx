import { getUnsubscribe } from "@/services/getUnsubscribe";

interface ISubscriptionIdProps {
    id:string
}

export const UserSettingsUnsubscribe = ({id}: ISubscriptionIdProps) => {
  const onDeletePhoto = async () => {
    try {
      const response = await getUnsubscribe(id);
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
    <span onClick={onDeletePhoto} className="settings_subscription_unsub">
      <img src="/img/settings/Crest.svg" alt="Delete" />
    </span>
  );
};
