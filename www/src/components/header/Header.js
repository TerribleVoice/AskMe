import React from "react";
import { Link } from "react-router-dom";

export default function Header() {
    return (
        <header className="header">
            <img src="img/search.svg" alt="" className="header__icon" />
            <input type="text" className="header__input" placeholder="Поиск автора" />
            <Link to="">
                <div className="header__signin">Войти</div>
            </Link>
            <Link to="/auth">
                <div className="header__signup">Зарегистрироваться</div>
            </Link>
        </header>

    );
}
