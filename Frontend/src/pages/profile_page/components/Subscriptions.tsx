import { IUserSubscriptions } from "@/models/IUserSubscriptions";
import { getUserSubscriptions } from "@/services/getUserSubscriptions";
import { useState, useEffect } from "react";
import { useParams, useNavigate, Link } from "react-router-dom";

const zaglushka: IUserSubscriptions[] = [
  {
    id: "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    authorId: "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    price: 0,
    name: "Первая подписка",
    description: "asdasdasdas",
    parentSubscriptionId: "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  },
  {
    id: "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    authorId: "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    price: 100,
    name: "Вторая подписка",
    description: "111111111111111111111",
    parentSubscriptionId: "3fa85f64-5717-4562-b3fc-2c963f66afb6",
  },
];

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
          setSubscriptions(subscriptions);
        } else {
          navigate("/404");
        }
      } catch (error) {
        console.log(error);
      }
    };

    fetchData();
  }, []);
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
            <Link to={`/${LoginName}/settings/edit_subscriptions`}>Редактировать</Link>
          </div>
        );
      })}
      <Link to={"create_subscription"} className="pp_body-create_subscr">
        ДОБАВИТЬ ПОДПИСКУ
      </Link>
    </div>
  );
};
