import { IUserSubscriptions } from "@/models/IUserSubscriptions";
import { getUserBoughtSubscriptions } from "@/services/getUserBoughtSubscriptions";
import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

const zaglushka: IUserSubscriptions[] = [
  {
    id: "Shaman",
    authorId: "1",
    price: 100,
    name: "Shaman",
    description: "eti rolexu mne muzh kupil",
    parentSubscriptionId: "asdjksla",
  },
  {
    id: "Shaman",
    authorId: "1",
    price: 100,
    name: "Shaman",
    description: "eti rolexu mne muzh kupil",
    parentSubscriptionId: "asdjksla",
  },
  {
    id: "Shaman",
    authorId: "1",
    price: 100,
    name: "Shaman",
    description: "eti rolexu mne muzh kupil",
    parentSubscriptionId: "asdjksla",
  },
  {
    id: "Shaman",
    authorId: "1",
    price: 100,
    name: "Shaman",
    description: "eti rolexu mne muzh kupil",
    parentSubscriptionId: "asdjksla",
  },
];

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
    <div>
      <h2>Подписки</h2>
      {boughtSubscription?.map((bs) => {
        return (
          <div
            key={bs.id}
            style={{ display: "flex", margin: "10px", flexDirection: "column" }}
          >
            <span>{bs.name}</span>
            <p>{bs.price}</p>
            <p>{bs.description}</p>
          </div>
        );
      })}
    </div>
  );
};
