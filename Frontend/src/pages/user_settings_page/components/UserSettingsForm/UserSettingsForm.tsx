import { IUserSettings } from "@/models/IUserSettings";
import { postUserSettingsForm } from "@/services/postUserSettingsForm";
import { useForm } from "react-hook-form";
import { useNavigate, useParams } from "react-router-dom";
import { UserSettingsPhoto } from "./UserSettingsPhoto";
import { UserSettingsDeletePhoto } from "./UserSettingsDeletePhoto";
import { IUserProfilePage } from "@/models/IUserProfilePage";
import { getUserProfilePage } from "@/services/getUserProfilePage";
import { useState, useEffect } from "react";

export const UserSettingsForm = () => {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<IUserSettings>();
  const { LoginName } = useParams();
  const navigation = useNavigate();
  const [profileData, setProfileData] = useState<IUserProfilePage>();
  const login = profileData?.login
  const links = profileData?.links
  const description = profileData?.description

  useEffect(() => {
    try {
      const fetchData = async () => {
        if (LoginName !== undefined) {
          const data = await getUserProfilePage(LoginName);
          if (data === undefined) {
            console.log("Ne uspeshno");
          } else {
            console.log(data);
            setProfileData(data);
          }
        } else {
          navigation("/404");
        }
      };
      fetchData();
    } catch (error) {
      console.log(error);
    }
  }, []);

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
          localStorage.removeItem("login");
          localStorage.setItem("login", data.login);

          navigation(`/${data.login}`);
        } else {
          const login = localStorage.getItem("login");
          navigation(`/${login}`);
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
          <input
            {...register("login", {
              required: true,
              setValueAs: (v) => (v === "" ? null : v),
            })}
            placeholder={login}
            defaultValue={login}
            type="text"
            name="login"
            id="login"
          />
          <label className="settings_caption" htmlFor="login">
            Имя будет показываться на вашей странице
          </label>
        </div>
        <div className="left-reg__login">
          <label htmlFor="email">Почта</label>
          <input
            {...register("email", {
              required: true,
              // setValueAs: (v) => (v === "" ? null : v),
            })}
            placeholder=""
            type="email"
            name="email"
            id="email"
          />
          <label className="settings_caption" htmlFor="login">
            Используется для входа в аккаунт
          </label>
        </div>
        <div className="left-reg__login">
          <label htmlFor="password">Пароль</label>
          <input
            {...register("password", {
              required: true,
              setValueAs: (v) => (v === "" ? null : v),
            })}
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
          <input
            {...register("links", {
              required: true,
              setValueAs: (v) => (v === "" ? null : v),
            })}
            placeholder={links}
            defaultValue={links}
            type="text"
            name="links"
            id="links"
          />
          <label className="settings_caption" htmlFor="login">
            Ссылки будут показываться на вашей странице
          </label>
        </div>
        <div className="settings_description">
          <label htmlFor="description">Описание</label>
          <textarea
            {...register("description", {
              required: true,
              setValueAs: (v) => (v === "" ? null : v),
            })}
            placeholder={description}
            defaultValue={description}
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
