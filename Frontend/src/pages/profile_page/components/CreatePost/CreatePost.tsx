import { IUserCreatePost } from "@/models/IUserProfilePage";
import { userCreatePost } from "@/services/postUserPost";
import { useForm } from "react-hook-form";


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
    <div className="pp_post__create">
      <form onSubmit={handleSubmit(onCreatePost)}>
      <div className="left-reg__login">
          <label htmlFor="content">Пост</label>
          <input
            {...register("content", { required: true })}
            type="text"
            id="content"
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
        <div className="left-reg__password">
          <label htmlFor="subscriptionName">Какая подписка</label>
          <input
            {...register("subscriptionName", { required: true })}
            type="text"
            id="subscriptionName"
          />
        </div>
        <div className="left-reg__submit">
          <button type="submit">Опубликовать</button>
        </div>
      </form>
    </div>
  );
};
