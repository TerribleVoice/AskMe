import { IUserSubscriptions } from "@/models/IUserSubscriptions";
import { getUserSubscriptions } from "@/services/getUserSubscriptions";
import { useState, useEffect } from "react";
import { useParams, useNavigate } from "react-router-dom";

export const SubscriptionsCheckBox = (register: any) => {
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
    <div className="create_post_subscriptions_wrapper">
      <p className="create_post_subscriptions_header">
        К КАКОЙ ПОДПИСКЕ ОТНОСИТСЯ ПОСТ?
      </p>
      {subscriptions?.map((subscription) => {
        return (
          <div key={subscription.id} className="create_post_subscriptions">
            <div className="pp_subscription_name_price">
              <div className="pp_subscription_name">{subscription.name}</div>
              <div className="pp_subscription_price">
                {subscription.price} рублей в месяц
              </div>
            </div>
            <div className="subscription_input">
              <label htmlFor="title">Введите заголовок поста</label>
              <input
                {...register("subscriptionId", { required: true })}
                className="subscription_input_subscriptionId"
                type="text"
                id="title"
                name="title"
              />
            </div>
          </div>
        );
      })}
    </div>
  );
};
