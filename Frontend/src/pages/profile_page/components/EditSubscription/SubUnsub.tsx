import { getSubscribe } from "@/services/getSubscribe";
import { getUnsubscribe } from "@/services/getUnsubscribe";
import { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import { IUserSubscriptionsProps } from "../Subscriptions";

export const SubUnsub = ({ subs }: IUserSubscriptionsProps) => {
  const { LoginName } = useParams();
  const yourLoginName = localStorage.getItem("login");
  const [subButtons, setSubButtons] = useState<{ [id: string]: boolean }>({});
  useEffect(() => {
    const initialSubButtonsState = subs.reduce(
      (acc, sub) => ({ ...acc, [sub.id]: sub.isBought }),
      {}
    );
    setSubButtons(initialSubButtonsState);
  }, [subs]);
  const onSubscribe = async (id: string) => {
    try {
      const response = await getSubscribe(id);
      console.log(response);
      if (response.status < 300) {
        setSubButtons((prevButtons) => ({ ...prevButtons, [id]: true }));
        // alert("Confirm");
      } else {
        // alert("Reject");
      }
    } catch (error) {
      console.error(error);
    }
  };

  const onUnsubscribe = async (id: string) => {
    try {
      const response = await getUnsubscribe(id);
      console.log(response);
      if (response.status < 300) {
        setSubButtons((prevButtons) => ({ ...prevButtons, [id]: false }));
        // console.log("Confirm");
      } else {
        // console.log("Reject");
      }
    } catch (error) {
      console.error(error);
    }
  };

  const sort_subs = subs.sort((a, b) => a.price - b.price)
  console.log(sort_subs)

  return (
    <>
      {subs.map((sub) => (
        <div key={sub.id} className="pp_subscription_not_yours">
          <div className="pp_subscription_name">{sub.name}</div>
          <div className="pp_subscription_price">
            {sub.price} рублей в месяц
          </div>
          <div className="pp_subscription_description">{sub.description}</div>
          {LoginName === yourLoginName ? (
            <Link state={sub} to={`/${LoginName}/edit_subscription/${sub.id}`}>
              Редактировать
            </Link>
          ) : (
            yourLoginName ? (
            <div
              onClick={() =>
                subButtons[sub.id] ? onUnsubscribe(sub.id) : onSubscribe(sub.id)
              }
              className="pp_body-create_subscr hover_create_subscr"
            >
              {subButtons[sub.id] ? "ОТПИСАТЬСЯ" : "ПОДПИСАТЬСЯ"}
            </div>) : null
          )}
        </div>
      ))}
    </>
  );
};
