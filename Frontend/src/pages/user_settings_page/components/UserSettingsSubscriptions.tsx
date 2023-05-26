import { IUserSubscriptions } from "@/models/IUserSubscriptions";
import { getUserBoughtSubscriptions } from "@/services/getUserBoughtSubscriptions";
import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { zaglushka } from "./subscriptions_data";
import { UserSettingsUnsubscribe } from "./UserSettingsUnsubscribe";

export const UserSettingsSubscriptions = () => {
  const [boughtSubscription, setBoughtSubscription] = useState<
    IUserSubscriptions[]
  >([]);
  const { LoginName } = useParams();
  useEffect(() => {
    try {
      const fetchData = async () => {
        if (LoginName !== undefined) {
          const data = await getUserBoughtSubscriptions(LoginName);
          if (data === undefined) {
            setBoughtSubscription(zaglushka);
          } else {
            console.log(data)
            setBoughtSubscription(data);
          }
        } else {
          console.log("/404");
        }
      };
      fetchData();
    } catch (error) {
      console.log(error);
    } finally {
      setBoughtSubscription(zaglushka);
    }
  }, [LoginName]);

  return (
    <div className="settings_form_wrapper">
      <h1>Подписки</h1>
      <div className="settings_subscription_wrapper">
        {boughtSubscription?.map((bs) => {
          return (
            <div key={bs.id} className="settings_subscription_card">
              <UserSettingsUnsubscribe id={bs.id}/>
              <span className="settings_subscription_name">{bs.name}</span>
              <p className="settings_subscription_description">
                {bs.description}
              </p>
              <p className="settings_subscription_price">{bs.price} RUB в месяц</p>
            </div>
          );
        })}
      </div>
    </div>
  );
};
