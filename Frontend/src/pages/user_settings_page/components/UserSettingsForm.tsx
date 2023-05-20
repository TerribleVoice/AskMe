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
  const { LoginName } = useParams();

  const onSettingsSubmit = async (data: IUserSettings) => {
    try {
      console.log(data);
      const response = await postUserSettingsForm({
        ...data,
        oldLogin: LoginName!,
      });
      console.log(response);
      if (response.status < 300) {
        alert("Confirm");
      } else {
        alert("Reject");
      }
    } catch (error) {
      console.error(error);
    }
  };
  return (
    <div className="settings_form_wrapper">
      <h1>Профиль</h1>
      <form className="settings_form" onSubmit={handleSubmit(onSettingsSubmit)}>
        <div className="left-reg__login">
          <label htmlFor="login">Логин</label>
          <input {...register("login")} type="text" name="login" id="login" />
        </div>
        <div className="left-reg__login">
          <label htmlFor="email">Почта</label>
          <input {...register("email")} type="email" name="email" id="email" />
        </div>
        <div className="left-reg__login">
          <label htmlFor="password">Пароль</label>
          <input
            {...register("password")}
            type="password"
            name="password"
            id="password"
          />
        </div>
        <div className="left-reg__login">
          <label htmlFor="links">Ссылки</label>
          <input {...register("links")} type="text" name="links" id="links" />
        </div>
        <div className="settings_description">
          <label htmlFor="description">Описание</label>
          <textarea
            {...register("description")}
            name="description"
            id="description"
          />
        </div>
        <div className="left-reg__submit">
          <button type="submit">Сохранить</button>
        </div>
      </form>
    </div>
  );
};
