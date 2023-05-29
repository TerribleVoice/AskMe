import { IUserSubscriptions } from "@/models/IUserSubscriptions";
import { getUserBoughtSubscriptions } from "@/services/getUserBoughtSubscriptions";
import { useEffect, useLayoutEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { getUnsubscribe } from "@/services/getUnsubscribe";

export const UserSettingsSubscriptions = () => {
  const [boughtSubscription, setBoughtSubscription] = useState<IUserSubscriptions[]>([]);
  useLayoutEffect(() => {
    window.scrollTo(0, 0);
  }, []);
  const { LoginName } = useParams();
  useEffect(() => {
    try {
      const fetchData = async () => {
        if (LoginName !== undefined) {
          const data = await getUserBoughtSubscriptions(LoginName);
          if (data === undefined) {
            // setBoughtSubscription(zaglushka);
          } else {
            console.log(data);
            setBoughtSubscription(data);
          }
        } else {
          console.log("/404");
        }
      };
      fetchData();
    } catch (error) {
      console.log(error);
    }
  }, [LoginName]);

  const [deletedSubscriptions, setDeletedSubscriptions] = useState<string[]>([]);

  const onDeletePhoto = async (id: string) => {
    try {
      const response = await getUnsubscribe(id);
      console.log(response);
      if (response.status < 300) {
        setDeletedSubscriptions((prevDeletedSubscriptions) => [...prevDeletedSubscriptions, id]);
      } else {
        alert("Reject");
      }
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="settings_form_wrapper">
      <h1>Подписки</h1>
      <div className="settings_subscription_wrapper">
        {boughtSubscription?.map((bs) => {
          const isDeleted = deletedSubscriptions.includes(bs.id);
          return (
            <div
              key={bs.id}
              className={`settings_subscription_card ${isDeleted ? "none" : ""}`}
            >
              <span
                onClick={() => onDeletePhoto(bs.id)}
                className="settings_subscription_unsub"
              >
                <img src="/img/settings/Crest.svg" alt="Delete" />
              </span>
              <img src="/img/NoUserPhoto.svg" alt="subset" style={{margin: "10px"}} />
              <span className="settings_subscription_name">{bs.name}</span>
              <p className="settings_subscription_description">
                {bs.description}
              </p>
              <p className="settings_subscription_price">
                {bs.price} RUB в месяц
              </p>
            </div>
          );
        })}
      </div>
    </div>
  );
};
