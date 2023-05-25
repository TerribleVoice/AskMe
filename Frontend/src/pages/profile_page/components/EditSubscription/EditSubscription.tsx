import { GoBack } from "@/components/GoBack";
import { IUserEditSubscription } from "@/models/IUserSubscriptions";
import { userCreateSubscription } from "@/services/postUserCreateSubscription";
import { userEditSubscription } from "@/services/postUserEditSubscription";
import { useForm } from "react-hook-form";
import { useParams } from "react-router-dom";
import { DeleteSubscription } from "./DeleteSubscription";

export const EditSubscription = () => {
  const {
    register,
    handleSubmit,
    reset,
    formState: { errors }, // нужен ли??
  } = useForm<IUserEditSubscription>();
  const { id } = useParams();

  const onEditSubscription = async (data: IUserEditSubscription) => {
    try {
      console.log(data);
      const response = await userEditSubscription(data, id!);
      console.log(response);
      if (response.status < 300) {
        console.log(response);
      } else {
        reset();
        alert("LSADJ:LASDJLA");
      }
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="subscription_create_wrapper">
      <aside className="subscription_aside_left">
        <GoBack />
      </aside>
      <div className="subscription_create">
        <DeleteSubscription />
        <h2>Редактирование подписки</h2>
        <form
          className="subscription_form"
          onSubmit={handleSubmit(onEditSubscription)}
        >
          <div className="subscription_input">
            <label htmlFor="name">Название подписки</label>
            <input
              className=""
              {...register("name", { required: true })}
              type="text"
              id="name"
              name="name"
            />
            <label className="settings_caption" htmlFor="name">
              Это будет названием данного уровня подписки
            </label>
          </div>
          {/* <div className="subscription_image">
                <label htmlFor="parentSubscriptionId">Обложка</label>
                <label className="custom_file_upload">
                  <input
                    {...register("parentSubscriptionId", )}
                    type="file"
                    id="parentSubscriptionId"
                    name="parentSubscriptionId"
                  />
                  ВЫБРАТЬ ФАЙЛ
                </label>
                <label className="settings_caption" htmlFor="description">
                  Рекомендуемый размер 240х150 рх
                </label>
              </div> */}
          <div className="subscription_description">
            <label htmlFor="description">Описание подписки</label>
            <textarea
              {...register("description", { required: true })}
              id="description"
              name="description"
            />
            <label className="settings_caption" htmlFor="description">
              Описание данного уровня подписки
            </label>
          </div>
          <div className="subscription_input">
            <label htmlFor="price">Стоимость месячной подписки (в RUB)</label>
            <input
              {...register("price", { required: true })}
              type="number"
              name="price"
              id="price"
              min={0}
              max={150000}
            />
            <label className="settings_caption" htmlFor="price">
              Максимальная стоимость подписки 150 000 RUB
            </label>
          </div>
          <div className="left-reg__submit submit_form">
            <button type="submit">Редактировать</button>
          </div>
        </form>
      </div>
    </div>
  );
};
