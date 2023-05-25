import { GoBack } from "@/components/GoBack";
import { IUserCreatePost } from "@/models/IUserPosts";
import { userCreatePost } from "@/services/postUserPost";
import { useForm } from "react-hook-form";


export const CreatePost = () => {
  const {
    register,
    handleSubmit,
    reset,
    formState: { errors }, // нужен ли??
  } = useForm();

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
        <form
          className="subscription_form"
          // onSubmit={handleSubmit(onCreatePost)}
        >
          <div className="subscription_input">
            <label htmlFor="name">Введите заголовок поста</label>
            <input
              className=""
              {...register("name", { required: true })}
              type="text"
              id="name"
              name="name"
            />
          </div>
          <div className="subscription_description">
            <label htmlFor="description">Описание поста</label>
            <textarea
              {...register("description", { required: true })}
              id="description"
              name="description"
            />
          </div>
          <div className="file_post">
            <label htmlFor="parentSubscriptionId">Фото или видео</label>
            <label className="custom_file_upload_post">
              <input
                {...register("parentSubscriptionId", { required: true })}
                type="file"
                id="parentSubscriptionId"
                name="parentSubscriptionId"
              />
              ВЫБРАТЬ ФАЙЛ
            </label>
          </div>
          <div className="left-reg__submit submit_form">
            <button type="submit">Создать</button>
          </div>
        </form>
      </div>
    </div>
  );
};
