import { Link } from "react-router-dom";

export const Header = () => {
    const login = localStorage.getItem("login");

    const button = login ? (
        <button type="button" className="header__signup" onClick={() => { localStorage.clear(); document.location.reload();}}>
            Выйти
        </button>
    ) : (
        <Link to="/auth">
            <button type="button" className="header__signup">
                Войти
            </button>
        </Link>
    );

    return (
        <header className="header">
            <div className="header__logo">
                <Link to="/">
                    <img src="img/profile/logo.png" alt="logo"></img>
                </Link>
            </div>
            <img src="img/search.svg" alt="" className="header__icon" />
            <input type="text" className="header__input" placeholder="Поиск автора" />
            {button}
        </header>
    );
}
