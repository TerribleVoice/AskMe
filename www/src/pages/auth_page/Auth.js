import React, {useState} from 'react'
import {useNavigate} from "react-router-dom";
import './Auth.css'
import {useLocation} from "react-router-dom";
import axios, {Axios} from 'axios';

export default function Auth() {
    const navigate = useNavigate();
    const location = useLocation();
    const [register, setRegister] = useState(() => {
        return {
            login: "123",
            password: "123",
            mail: "123",
            errorMsg: ""
        }
    })

    const onAuthClick = event => {
        event.target.classList.add('active-btn');
        event.target.previousElementSibling.classList.remove('active-btn');
        document.getElementById('mail').setAttribute('type', 'text')
        document.querySelector('.left-reg__mail').classList.add('hide');
        document.querySelector('.left-reg__isAuthor').classList.add('hide');
    }

    const onRegClick = event => {
        event.target.classList.add('active-btn');
        event.target.nextElementSibling.classList.remove('active-btn');
        document.getElementById('mail').setAttribute('type', 'email')
        document.querySelector('.left-reg__mail').classList.remove('hide');
        document.querySelector('.left-reg__isAuthor').classList.remove('hide');
    }

    const changeInput = event => {
        event.persist()
        setRegister(prev => {
            return {
                ...prev,
                [event.target.name]: event.target.value,
            }
        })
    }

    const handleLogin = (event) => {
        let isAuth = document.querySelector('.left-reg__mail').classList.contains('hide')
        if (isAuth) {
            axios({
                method: 'post',
                withCredentials: true,
                url: "http://localhost:7279/User/login?login=" + register.login + "&password=" + register.password,
                headers: {accept: '*/*', credentials: 'include'}
            })
                .then(res => {
                    localStorage.setItem("login", register.login)
                    navigate('/')
                }).catch(err => alert(err))
        } else {
            let isAuthor = document.getElementById('isAuthor').checked
            axios({
                method: 'post',
                url: "http://localhost:7279/User/create",
                withCredentials: true,
                headers: {accept: '*/*', 'Content-Type': 'application/json', credentials: 'include'},
                data: {
                    login: register.login,
                    email: register.mail,
                    password: register.password,
                    isAuthor: isAuthor
                }
            }).then(res => {
                },
                error => {
                })
        }
        event.preventDefault();
        location.reload();
    };

    return (
        <div className="wrapper">
            <div className="main">
                <img className="main__angel" src="angel.png" alt=""/>
                <div className="reg">
                    <div className="reg__left left-reg">
                        <div className="left-reg__choose">
                            <div className="left-reg__registation active-btn"
                                 onClick={onRegClick}>Регистрация
                            </div>
                            <div className="left-reg__auth" onClick={onAuthClick}>Авторизация
                            </div>
                        </div>
                        <div className="left-reg__welcome">Добро пожаловать</div>
                        <div className="left-reg__text">Введите адрес электронной почты, придумайте логин и
                            пароль
                        </div>
                        <form onSubmit={handleLogin} className="left-reg__form">
                            <div className="left-reg__mail">
                                <label htmlFor="mail">Электронная почта</label>
                                <input value={register.mail}
                                       onInput={changeInput} type="email" id="mail" name="mail"/>
                            </div>
                            <div className="left-reg__login">
                                <label htmlFor="login">Логин</label>
                                <input value={register.login}
                                       onInput={changeInput} type="text" id="login" name="login"/>
                            </div>
                            <div className="left-reg__password">
                                <label htmlFor="password">Пароль</label>
                                <input value={register.password}
                                       onInput={changeInput} type="password" id="password" name="password"/>
                            </div>
                            <div className="left-reg__isAuthor">
                                <input  type="checkbox" id="isAuthor" name="isAuthor"/>
                                <label htmlFor="mail">Хотите стать автором?</label>
                            </div>
                            <div className="left-reg__submit">
                                <button type="submit">Далее</button>
                            </div>
                        </form>
                    </div>
                    <div className="reg__right">
                        <img src="woman.jpg" alt/>
                    </div>
                </div>
            </div>
        </div>
    )
}