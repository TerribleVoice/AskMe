import { getSubscribe } from "@/services/getSubscribe";
import { getUnsubscribe } from "@/services/getUnsubscribe";
import { useState } from "react";
import { useParams, Link } from "react-router-dom";
import { IUserSubscriptionsProps } from "../Subscriptions";

export const SubUnsub = ({ subs }: IUserSubscriptionsProps) => {
  const { LoginName } = useParams();
  const yourLoginName = localStorage.getItem("login");
  const [subButtons, setSubButtons] = useState<{ [id: string]: boolean }>({});

  const onSubscribe = async (id: string) => {
    try {
      const response = await getSubscribe(id);
      console.log(response);
      if (response.status < 300) {
        setSubButtons((prevButtons) => ({ ...prevButtons, [id]: false }));
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
        setSubButtons((prevButtons) => ({ ...prevButtons, [id]: true }));
        // console.log("Confirm");
      } else {
        // console.log("Reject");
      }
    } catch (error) {
      console.error(error);
    }
  };

  // const sort_subs = subs.sort((a, b) => a.price - b.price)
  // console.log(sort_subs)

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
            <Link state={subs} to={`/${LoginName}/edit_subscription/${sub.id}`}>
              Редактировать
            </Link>
          ) : (
            <div
              onClick={() =>
                subButtons[sub.id] ? onSubscribe(sub.id) : onUnsubscribe(sub.id)
              }
              className="pp_body-create_subscr hover_create_subscr"
            >
              {subButtons[sub.id] ? "ПОДПИСАТЬСЯ" : "ОТПИСАТЬСЯ"}
            </div>
          )}
        </div>
      ))}
    </>
  );
};
