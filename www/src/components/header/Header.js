import React from "react";
import { Link } from "react-router-dom";

export default function Header() {
    return (
        <header className="header">
            <div class="header__logo">
            <Link to="/">
                <img src="img/profile/logo.png" alt="logo"></img>
            </Link>
            </div>
            <img src="img/search.svg" alt="" className="header__icon" />
            <input type="text" className="header__input" placeholder="Поиск автора" />
            <Link to="/auth">
                <div className="header__signup">Войти</div>
            </Link>
        </header>
    );
}
