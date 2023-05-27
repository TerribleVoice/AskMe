import { IUserSubscriptions } from "@/models/IUserSubscriptions";
import { useParams, useNavigate, Link } from "react-router-dom";
import { SubUnsub } from "./EditSubscription/SubUnsub";

export interface IUserSubscriptionsProps {
  subs: IUserSubscriptions[];
}

export const Subscriptions = ({ subs }: IUserSubscriptionsProps) => {
  const { LoginName } = useParams();
  const yourLoginName = localStorage.getItem("login");
  const navigate = useNavigate();

  return (
    <div className="pp_subscriptions_wrapper">
      <p className="pp_subscriptions_header">УРОВНИ ПОДПИСКИ</p>

      <SubUnsub subs={subs} />
      {LoginName === yourLoginName ? (
        <Link
          to="create_subscription"
          onClick={() => navigate(`/${LoginName}`)}
          className="pp_body-create_subscr"
        >
          ДОБАВИТЬ ПОДПИСКУ
        </Link>
      ) : null}
    </div>
  );
};
