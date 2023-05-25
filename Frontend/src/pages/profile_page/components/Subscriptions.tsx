import { IUserSubscriptions } from "@/models/IUserSubscriptions";
import { getUserSubscriptions } from "@/services/getUserSubscriptions";
import { useState, useEffect } from "react";
import { useParams, useNavigate, Link } from "react-router-dom";

export const Subscriptions = () => {
  const { LoginName } = useParams();
  const navigate = useNavigate();
  const [subscriptions, setSubscriptions] = useState<IUserSubscriptions[]>();

  useEffect(() => {
    const fetchData = async () => {
      try {
        if (LoginName !== undefined) {
          const data = await getUserSubscriptions(LoginName);
          console.log(data);
          setSubscriptions(data);
        } else {
          navigate("/404");
        }
      } catch (error) {
        console.log(error);
      }
    };

    fetchData();
  }, [LoginName]);
  console.log(subscriptions);
  return (
    <div className="pp_subscriptions_wrapper">
      <p className="pp_subscriptions_header">УРОВНИ ПОДПИСКИ</p>
      {subscriptions?.map((subscription) => {
        return (
          <div key={subscription.id} className="pp_subscription">
            <div className="pp_subscription_name">{subscription.name}</div>
            <div className="pp_subscription_price">
              {subscription.price} рублей в месяц
            </div>
            <div className="pp_subscription_description">
              {subscription.description}
            </div>
            <Link to={`/${LoginName}/edit_subscription/${subscription.id}`}>Редактировать</Link>
          </div>
        );
      })}
      <Link to={"create_subscription"} className="pp_body-create_subscr">
        ДОБАВИТЬ ПОДПИСКУ
      </Link>
    </div>
  );
};
