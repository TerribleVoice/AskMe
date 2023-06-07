import { IUserSettings } from "@/models/IUserSettings";
import { postUserSettingsForm } from "@/services/postUserSettingsForm";
import { useForm } from "react-hook-form";
import { useNavigate, useParams } from "react-router-dom";
import { UserSettingsPhoto } from "./UserSettingsPhoto";
import { UserSettingsDeletePhoto } from "./UserSettingsDeletePhoto";
import { IUserProfilePage } from "@/models/IUserProfilePage";
import { getUserProfilePage } from "@/services/getUserProfilePage";
import { useState, useEffect, useLayoutEffect } from "react";

export const UserSettingsForm = () => {
  const LoginName = localStorage.getItem("login");
  const navigation = useNavigate();
  useLayoutEffect(() => {
    window.scrollTo(0, 0);
  }, []);
  const [profileData, setProfileData] = useState<IUserProfilePage | null>(null);

  useEffect(() => {
    const fetchData = async () => {
      if (LoginName !== undefined) {
        try {
          const data = await getUserProfilePage(LoginName!);
          if (data === undefined) {
            console.log("Ne uspeshno");
          } else {
            console.log(data);
            setProfileData(data);
          }
        } catch (error) {
          console.log(error);
        }
      } else {
        navigation("/404");
      }
    };
    fetchData();
  }, []);

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<IUserSettings>({
    defaultValues: {
      login: LoginName!,
      email: "",
      password: "",
      links: profileData?.links || "",
      description: profileData?.description || "",
    },
  });

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

  if (profileData === null) {
    return <div>Loading...</div>;
  }
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
              // setValueAs: (v) => (v === "" ? v : v),
            })}
            placeholder={LoginName!}
            // defaultValue={login}
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
              // setValueAs: (v) => (v === "" ? v : v),
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
              // setValueAs: (v) => (v === "" ? v : v),
            })}
            type="password"
            name="password"
            id="password"
          />
          <label className="settings_caption" htmlFor="login">
            Используется для входа в аккаунт
          </label>
        </div>
        <div className="settings_links">
          <label htmlFor="links">Ссылки</label>
          <textarea
            {...register("links", {
              // setValueAs: (v) => (v === "" ? v : v),
            })}
            // placeholder={profileData?.links === null ? "" : profileData?.links}
            // defaultValue={profileData?.links === null ? "" : profileData?.links}
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
              // setValueAs: (v) => (v === "" ? v : v),
            })}
            // placeholder={profileData?.description === null ? "" : profileData?.description}
            // defaultValue={profileData?.description === null ? "" : profileData?.description}
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
