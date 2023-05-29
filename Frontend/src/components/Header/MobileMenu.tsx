import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { AiOutlineMenu, AiOutlineClose } from "react-icons/ai";
import { IUserProfilePage } from "@/models/IUserProfilePage";
import { getUserProfilePage } from "@/services/getUserProfilePage";

const zaglushka: IUserProfilePage = {
  login: "Login1",
  description:
    "Description1 Description1 Description1 Description1 Description1 Description1 Description1 Description1 Description1 Description1 ",
  profileImageUrl: "/img/NoUserPhoto.svg",
  links: "https://link1.com",
};

export const MobileMenu = () => {
  const login = localStorage.getItem("login");
  const [navigation, setNavigation] = useState(false);
  const [settings, setSettings] = useState(false);
  const [profileData, setProfileData] = useState<
    IUserProfilePage | undefined
  >();
  const LoginName = localStorage.getItem("login");

  const handleNavigation = () => {
    setNavigation(!navigation);
  };
  const handleSettings = () => {
    setSettings(!settings);
  };
  useEffect(() => {
    try {
      const fetchData = async () => {
        if (LoginName !== undefined) {
          const data = await getUserProfilePage(LoginName!);
          if (data === undefined) {
            setProfileData(zaglushka);
          } else {
            console.log(data);
            setProfileData(data);
          }
        }
      };
      fetchData();
    } catch (error) {
      console.log(error);
    }
  }, [LoginName]);
  const image = profileData?.profileImageUrl
    ? "/img/NoUserPhoto.svg"
    : profileData?.profileImageUrl;
  return (
    <>
      <button className="menu-button" onClick={handleNavigation}>
        {navigation ? (
          <AiOutlineClose size={28} className="AiOutlineClose" />
        ) : (
          <AiOutlineMenu size={28} className="AiOutlineMenu" />
        )}
      </button>
      <div className={navigation ? "menu-side-open" : "menu-side-hidden"}>
        <div className="menu_profile_avatar">
          {profileData?.profileImageUrl !== null ? (
            <img className="pp_left__avatar" src={`${image}`} alt="avatar" />
          ) : (
            <img
              className="pp_left__avatar"
              src={`img/NoUserPhoto.svg`}
              alt="noava"
            />
          )}
          <span className="menu_login">{LoginName}</span>
        </div>
        <ul className="menu-content">
          <Link
            onClick={handleNavigation}
            className="menu__dropdown-link"
            to={login || ""}
          >
            <img
              className="menu_link_img"
              src="/img/settings/Userlogo.svg"
              alt="profile"
            />
            Профиль
          </Link>
          <Link
            onClick={handleNavigation}
            className="menu__dropdown-link"
            to={`feed`}
          >
            <img
              className="menu_link_img"
              src="/img/side_menu/FeedLogo.svg"
              alt="profile"
            />
            Лента
          </Link>
          <div
            onClick={handleSettings}
            className="menu__dropdown-link menu_settings_link"
          >
            <img
              className="menu_link_img"
              src="/img/side_menu/SettingsLogo.svg"
              alt="profile"
            />
            Настройки
            {settings ? (
              <div className="menu_sub-settings">
                <Link
                  onClick={handleNavigation}
                  className="menu__dropdown-link"
                  to={`${login}/settings/profile`}
                >
                  <img
                    className="menu_link_img"
                    src="/img/settings/Userlogo.svg"
                    alt="profile"
                  />
                  Настройка профиля
                </Link>
                <Link
                  onClick={handleNavigation}
                  className="menu__dropdown-link"
                  to={`${login}/settings/subscriptions`}
                >
                  <img
                    className="menu_link_img"
                    src="/img/settings/SubscrLogo.svg"
                    alt="profile"
                  />
                  Мои подписки
                </Link>
              </div>
            ) : (
              <></>
            )}
          </div>
          <Link
            onClick={handleNavigation}
            className={`menu__dropdown-link ${settings ? "menu-sublink" : ""}`}
            to={`https://t.me/AskMeDonateBot`}
          >
            <img className="menu_link_img" src="/img/side_menu/TelegramLogoS.svg" alt="telega" />
            Telegram Бот
          </Link>
          <Link
            className={`menu__dropdown-link ${settings ? "menu-sublink" : ""}`}
            to={"/"}
            reloadDocument
            onClick={() => {
              localStorage.clear();
            }}
          >
            <img className="menu_link_img" src="/img/side_menu/ExitIcon.svg" alt="exit" />
            Выйти
          </Link>
        </ul>
      </div>
    </>
  );
};
