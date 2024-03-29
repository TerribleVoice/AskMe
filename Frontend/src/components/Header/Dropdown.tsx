import { Link } from "react-router-dom";

export const Dropdown = () => {
  const login = localStorage.getItem("login");

  const handleLogin = (login: string | null): string => {
    if (login && login.length > 14) {
      const shortLogin = login.substring(0, 14) + "...";
      return shortLogin;
    } else {
      return login || "";
    }
  };

  return (
    <div className="header__dropdown">
      <button className="header__dropdown-button">{handleLogin(login)}</button>
      <div className="header__dropdown-content">
        <Link className="header__dropdown-link" to={login || ""}>
          Профиль
        </Link>
        <Link className="header__dropdown-link" to={`feed`}>
          Лента
        </Link>
        <Link
          className="header__dropdown-link"
          to={`${login}/settings/profile`}
        >
          Настройки
        </Link>
        <Link
          className="header__dropdown-link"
          to={`https://t.me/AskMeDonateBot`}
        >
          Telegram Бот
        </Link>
        <Link
          className="header__dropdown-link"
          to={"/"}
          reloadDocument
          onClick={() => {
            localStorage.clear();
          }}
        >
          Выйти
        </Link>
      </div>
    </div>
  );
};
