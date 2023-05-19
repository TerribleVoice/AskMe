import { IUserCreateSubscription } from "@/models/IUserSubscriptions";
import { userCreateSubscription } from "@/services/postUserSubscription";
import { useForm } from "react-hook-form";

export const CreateSubscription = () => {
  const {
    register,
    handleSubmit,
    reset,
    formState: { errors }, // нужен ли??
  } = useForm<IUserCreateSubscription>();

  const onCreateSubscription = async (data:IUserCreateSubscription) => {
    try {
      console.log(data);
      const response = await userCreateSubscription(data);
      console.log(response);
      if (response.status < 300) {
        console.log(response)
      } else {
        reset();
        alert("LSADJ:LASDJLA");
      }
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="pp_post__create">
      <form onSubmit={handleSubmit(onCreateSubscription)}>
      <div className="left-reg__login">
          <label htmlFor="name">Название подписки</label>
          <input
            {...register("name", { required: true })}
            type="text"
            id="name"
          />
        </div>
        <div className="left-reg__password">
          <label htmlFor="description">Описание</label>
          <input
            {...register("description", { required: true })}
            type="text"
            id="description"
          />
        </div>
        <div className="left-reg__password">
          <label htmlFor="parentSubscriptionId">Id подписки</label>
          <input
            {...register("parentSubscriptionId", { required: true })}
            type="text"
            id="parentSubscriptionId"
          />
        </div>
        <div className="left-reg__password">
          <label htmlFor="price">Цена</label>
          <input
            {...register("price", { required: true })}
            type="number"
            id="price"
          />
        </div>
        <div className="left-reg__submit">
          <button type="submit">Создать</button>
        </div>
      </form>
    </div>
  );
};
