import { NavLink, Navigate, Outlet } from "react-router-dom";

export const FeedLayout = () => {
  const login = localStorage.getItem("login");
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
            to={`/${login}/settings/profile`}
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
        </nav>
      </aside>
    </div>
  );
};
