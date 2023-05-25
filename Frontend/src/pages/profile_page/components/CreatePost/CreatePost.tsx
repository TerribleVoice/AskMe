import { GoBack } from "@/components/GoBack";
import { IUserCreatePost } from "@/models/IUserPosts";
import { userCreatePost } from "@/services/postUserPost";
import { useForm } from "react-hook-form";
import { Subscriptions } from "../Subscriptions";
import { SubscriptionsCheckBox } from "./SubscriptionsCheckBox";


export const CreatePost = () => {
  const {
    register,
    handleSubmit,
    reset,
    formState: { errors }, // нужен ли??
  } = useForm<IUserCreatePost>();

  const onCreatePost = async (data:IUserCreatePost) => {
    try {
      console.log(data);
      const response = await userCreatePost(data);
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
    <div className="subscription_create_wrapper">
      <aside className="subscription_aside_left">
        <GoBack />
      </aside>
      <div className="subscription_create">
        <h2>Создание нового Поста</h2>
          <SubscriptionsCheckBox />
        <form
          className="subscription_form"
          onSubmit={handleSubmit(onCreatePost)}
        >
          <div className="subscription_input">
            <label htmlFor="title">Введите заголовок поста</label>
            <input
              className=""
              {...register("title", { required: true })}
              type="text"
              id="title"
              name="title"
            />
          </div>
          <div className="subscription_description">
            <label htmlFor="content">Описание поста</label>
            <textarea
              {...register("content", { required: true })}
              id="content"
              name="content"
            />
          </div>
          <div className="file_post">
            <label htmlFor="files">Фото или видео</label>
            <label className="custom_file_upload">
              <input
                {...register("files", { required: true })}
                type="file"
                id="files"
                name="files"
              />
              ВЫБРАТЬ ФАЙЛ
            </label>
          </div>
          <div className="subscription_input">
            <label htmlFor="price">Стоимость поста</label>
            <input
              {...register("price", { required: true })}
              type="number"
              id="price"
              name="price"
              min={0}
              max={150000}
            />
          </div>
          <div className="left-reg__submit submit_form">
            <button type="submit">Создать</button>
          </div>
        </form>
      </div>
    </div>
  );
};
