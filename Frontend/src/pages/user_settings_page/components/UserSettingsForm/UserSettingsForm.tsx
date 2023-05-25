import { IUserSettings } from "@/models/IUserSettings";
import { postUserSettingsForm } from "@/services/postUserSettingsForm";
import { useForm } from "react-hook-form";
import { useNavigate, useParams } from "react-router-dom";
import { UserSettingsPhoto } from "./UserSettingsPhoto";
import { UserSettingsDeletePhoto } from "./UserSettingsDeletePhoto";

export const UserSettingsForm = () => {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<IUserSettings>();
  const { LoginName } = useParams();
  const navigation = useNavigate()

  const onSettingsSubmit = async (data: IUserSettings) => {
    try {
      console.log(data);
      const response = await postUserSettingsForm({
        ...data,
        oldLogin: LoginName!,
      });
      console.log(response);
      if (response.status < 300) {
        if (data.login) {
          localStorage.removeItem("login")
          localStorage.setItem("login", data.login);
           
          navigation(`/${data.login}`)
        } else {
          const login = localStorage.getItem("login")
          navigation(`/${login}`)
        }
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
      <UserSettingsPhoto />
      <UserSettingsDeletePhoto />
      <form className="settings_form" onSubmit={handleSubmit(onSettingsSubmit)}>
        <div className="left-reg__login">
          <label htmlFor="login">Имя</label>
          <input {...register("login")} type="text" name="login" id="login" />
          <label className="settings_caption" htmlFor="login">
            Имя будет показываться на вашей странице
          </label>
        </div>
        <div className="left-reg__login">
          <label htmlFor="email">Почта</label>
          <input {...register("email")} type="email" name="email" id="email" />
          <label className="settings_caption" htmlFor="login">
            Используется для входа в аккаунт
          </label>
        </div>
        <div className="left-reg__login">
          <label htmlFor="password">Пароль</label>
          <input
            {...register("password")}
            type="password"
            name="password"
            id="password"
          />
          <label className="settings_caption" htmlFor="login">
            Используется для входа в аккаунт
          </label>
        </div>
        <div className="left-reg__login">
          <label htmlFor="links">Ссылки</label>
          <input {...register("links")} type="text" name="links" id="links" />
          <label className="settings_caption" htmlFor="login">
            Ссылки будут показываться на вашей странице
          </label>
        </div>
        <div className="settings_description">
          <label htmlFor="description">Описание</label>
          <textarea
            {...register("description")}
            name="description"
            id="description"
          />
          <label className="settings_caption" htmlFor="login">
            Описание будет показываться на вашей странице
          </label>
        </div>
        <p className="left-reg__submit">
          <button type="submit">Сохранить</button>
        </p>
      </form>
    </div>
  );
};
