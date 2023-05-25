import { DebounceSearch } from "@/hooks/DebounceSearch";
import { Link } from "react-router-dom";

export const Header = () => {
  const login = localStorage.getItem("login");

  const handleLogin = (login: string) => {
    if (login && login.length > 14) {
      const shortLogin = login.substring(0, 14) + "...";
      return shortLogin;
    } else {
      return login;
    }
  };

  const buttons = login ? (
    <div className="header__dropdown">
      <button className="header__dropdown-button">{handleLogin(login)}</button>
      <div className="header__dropdown-content">
        <Link to={login}>Профиль</Link>
        <Link to={`feed`}>Лента</Link>
        <Link to={`${login}/settings`}>Настройки</Link>
        <Link
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
  ) : (
    <Link to="auth" className="header__signup">
      Войти
    </Link>
  );

  return (
    <header className="header">
      <Link to="/" className="header__logo">
        <img src="img/profile/logo.png" alt="logo"></img>
      </Link>
      <img src="img/search.svg" alt="" className="header__icon" />
      {/* <input type="text" className="header__input" placeholder="Поиск автора" /> */}
      <DebounceSearch />
      {buttons}
    </header>
  );
};
