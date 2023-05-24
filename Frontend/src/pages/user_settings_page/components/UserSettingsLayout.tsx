import { NavLink, Outlet, useLocation, useMatch } from "react-router-dom";

export const UserSettingsLayout = () => {
  const login = localStorage.getItem("login");

  const match = useMatch(":LoginName/settings/*");
  const url = match?.pathnameBase ?? "";
  return (
    <div className="settings_wrapper">
      <aside className="settings_aside_left">
        <nav className="settings_nav">
          <NavLink
            className={({ isActive }) =>
              isActive ? "settings_nav_link" : "settings_nav_link"
            }
            to={`/${login}`}
          >
            <img
              className="settings_img_link"
              src="/img/side_menu/Userlogo.svg"
              alt="settings_profile"
            />
            Профиль
          </NavLink>
          <NavLink
            className={({ isActive }) =>
              isActive ? "settings_nav_link active" : "settings_nav_link"
            }
            to={`${url}`}
          >
            <img
              className="settings_img_link"
              src="/img/side_menu/SettingsLogo.svg"
              alt="settings_subscription"
            />
            Настройки
          </NavLink>
          <NavLink
            className={({ isActive }) =>
              isActive ? "settings_nav_link active" : "settings_nav_link"
            }
            to={`/feed`}
          >
            <img
              className="settings_img_link"
              src="/img/side_menu/FeedLogo.svg"
              alt="settings_subscription"
            />
            Лента
          </NavLink>
        </nav>
      </aside>
      <Outlet />
      <aside className="settings_aside_right">
        <nav className="settings_nav">
          <NavLink
            className={({ isActive }) =>
              isActive ? "settings_nav_link active" : "settings_nav_link"
            }
            to={`${url}/profile`}
          >
            <img
              className="settings_img_link"
              src="/img/settings/Userlogo.svg"
              alt="settings_profile"
            />
            Настройки профиля
          </NavLink>
          <NavLink
            className={({ isActive }) =>
              isActive ? "settings_nav_link active" : "settings_nav_link"
            }
            to={`${url}/subscriptions`}
          >
            <img
              className="settings_img_link"
              src="/img/settings/SubscrLogo.svg"
              alt="settings_subscription"
            />
            Мои подписки
          </NavLink>
          <NavLink
            className={({ isActive }) =>
              isActive ? "settings_nav_link active" : "settings_nav_link"
            }
            to={`${url}/payments`}
          >
            <img
              className="settings_img_link"
              src="/img/settings/SubscrLogo2.svg"
              alt="settings_subscription"
            />
            Платежная информация
          </NavLink>
        </nav>
      </aside>
    </div>
  );
};
