import { DebounceSearch } from "@/components/Header/DebounceSearch";
import { Link } from "react-router-dom";
import { Dropdown } from "./Dropdown";
import { MobileMenu } from "./MobileMenu";

export const Header: React.FC = () => {
  const login = localStorage.getItem("login");

  return (
    <header className="header">
      <Link to="/" className="header__logo">
        <img src="img/profile/logo.png" alt="logo"></img>
      </Link>
      <img src="img/search.svg" alt="" className="header__icon" />
      <DebounceSearch />
      {login ? (
        <>
          <Dropdown />
          <MobileMenu />
        </>
      ) : (
        <Link to="auth" className="header__signup">
          Войти
        </Link>
      )}
    </header>
  );
};
