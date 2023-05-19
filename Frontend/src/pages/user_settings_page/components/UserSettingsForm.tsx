import { IUserSettings } from "@/models/IUserSettings";
import { postUserSettingsForm } from "@/services/postUserSettingsForm";
import { useForm } from "react-hook-form";
import { useParams } from "react-router-dom";

export const UserSettingsForm = () => {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<IUserSettings>();
  const {LoginName} = useParams()
  
  const onSettingsSubmit = async (data:IUserSettings) => {
    try {
      console.log(data);
      const response = await postUserSettingsForm({...data, oldLogin: LoginName!});
      console.log(response);
      if (response.status < 300) {
        alert("Confirm")
      } else {
        alert("Reject");
      }
    } catch (error) {
      console.error(error);
    }
  }

  return (
    <form onSubmit={handleSubmit(onSettingsSubmit)}>
      <div className="left-reg__login">
        <label htmlFor="login">Логин</label>
        <input {...register("login")} type="text" id="login" />
      </div>
      <div className="left-reg__login">
        <label htmlFor="email">Почта</label>
        <input {...register("email")} type="email" id="email" />
      </div>
      <div className="left-reg__login">
        <label htmlFor="password">Пароль</label>
        <input {...register("password")} type="password" id="password" />
      </div>
      <div className="left-reg__login">
        <label htmlFor="description">Описание</label>
        <input {...register("description")} type="text" id="description" />
      </div>
      <div className="left-reg__login">
        <label htmlFor="links">Ссылки</label>
        <input {...register("links")} type="text" id="links" />
      </div>
      <div className="left-reg__submit">
        <button type="submit">Сохранить</button>
      </div>
    </form>
  );
};
