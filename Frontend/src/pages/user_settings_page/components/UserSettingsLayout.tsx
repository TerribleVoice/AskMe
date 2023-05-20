import { NavLink, Outlet, useMatch, useNavigate } from "react-router-dom";

export const UserSettingsLayout = () => {
  const match = useMatch(":LoginName/settings/*");
  const url = match?.pathnameBase ?? "";
  return (
    <div className="settings_wrapper">
      <aside className="settings_aside_nav">
        <nav className="settings_nav">
          <NavLink className="settings_nav_link" to={`${url}/profile`}>Профиль</NavLink>
          <NavLink className="settings_nav_link" to={`${url}/subscriptions`}>Подписки</NavLink>
        </nav>
      </aside>
      <Outlet />
    </div>
  );
};
