import React from "react";
import { Link } from "react-router-dom";

export default function Header() {
    const userLogin = localStorage.getItem('login')
    let button
    if(userLogin){
        button = <Link to="/" onClick={()=> {localStorage.clear(); document.location.reload();}}>
                    <div className="header__signup">Выйти</div>
                </Link>
    }
    else{
        button = <Link to="/auth">
                    <div className="header__signup">Войти</div>
                </Link>
    }
    return (
        <header className="header">
            <div class="header__logo">
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
