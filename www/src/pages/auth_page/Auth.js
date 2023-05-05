import React, {useState} from 'react'
import {useNavigate} from "react-router-dom";
import './Auth.css'
import {useLocation} from "react-router-dom";
import axios, {Axios} from 'axios';//Регистрация ща не работает, AxiosError: Request failed with status code 401

export default function Auth() {
    const navigate = useNavigate();
    const location = useLocation();
    const [register, setRegister] = useState(() => {//что передать в форму
        return {
            login: "123",
            password: "123",
            mail: "123@mail.ru",
            errorMsg: ""
        }
    })

    const onAuthClick = event => {
        event.target.classList.add('active-btn');//добавляем класс активной кнопки(типо большая надпись)
        event.target.previousElementSibling.classList.remove('active-btn');//убираем этот же класс из предыдущей надписи
        document.getElementById('mail').setAttribute('type', 'text')//отмена проверки почты
        document.querySelector('.left-reg__mail').classList.add('hide');//скрываем поля которые не должны видеть
        document.querySelector('.left-reg__isAuthor').classList.add('hide');//скрываем поля которые не должны видеть
    }

    const onRegClick = event => {
        event.target.classList.add('active-btn');//добавляем класс активной кнопки(типо большая надпись)
        event.target.nextElementSibling.classList.remove('active-btn');//убираем этот же класс из предыдущей надписи
        document.getElementById('mail').setAttribute('type', 'email')//будет проверять почта ли это (есть @ичето.еще)
        document.querySelector('.left-reg__mail').classList.remove('hide');//скрываем поля которые не должны видеть
        document.querySelector('.left-reg__isAuthor').classList.remove('hide');//скрываем поля которые не должны видеть
    }

    const changeInput = event => {//чтобы записать из формы в переменные
        event.persist()
        setRegister(prev => {
            return {
                ...prev,
                [event.target.name]: event.target.value,//TODO: поискать че оно делает
            }
        })
    }

    const handleLogin = (event) => { //объявление функции для передачи в форму типо по нажатию кнопки
        let isAuth = document.querySelector('.left-reg__mail').classList.contains('hide')//переключение класса для показа
        if (isAuth) {
            axios({//библа для нодджс для http запросов, можно юзать потом для других штук в проекте
                method: 'post',//тип хттп запроса
                withCredentials: true,//для прокидки куки
                url: "http://localhost:5131/User/login?login=" + register.login + "&password=" + register.password,//7279 это порт из апи, откуда он будет слушать,,, константа реджистер сверху, в ней написали что передать в форму
                headers: {accept: '*/*', credentials: 'include'}//для куки
            })
                .then(res => {//запрос прошёл успешно
                    localStorage.setItem("login", register.login)//хранение логина в браузере
                    navigate('/')//отправка на главную
                }).catch(err => alert(err))//если не удался выводит ошибку
        } else {
            let isAuthor = document.getElementById('isAuthor').checked//регистрация
            axios({//вызов метода апи, можно юзать потом для других штук в проекте
                method: 'post',
                url: "http://localhost:5131/User/create",//можно спросить у михи че как используется в свагере
                withCredentials: true,//для прокидки куки
                headers: {accept: '*/*', 'Content-Type': 'application/json', credentials: 'include'},
                data: {//возможно регистрация не работает из-за обновленного бека, там больше полей для данных, не все параметры передаются(смотреть свагер)
                    login: register.login,
                    email: register.mail,
                    password: register.password,
                    isAuthor: isAuthor
                }
            }).then(res => {//обработка результата для авторизации и регистрации, рес=ответ от сервера
                }
                ).catch(err => alert(err))  
        }
        event.preventDefault();//костыль чтобы не слетели цсс стили при авторизации
        location.reload();//часть костыля, перезагружает страницу
    };
/*
Handlelogin написанный сверху приравнивается к onsumbit(при нажатии на кнопку)
value={register.mail} value={register.login}
onClick={onRegClick} и  onClick={onAuthClick} переключатели авторизации и регистрации
*/
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
                                <input type="checkbox" id="isAuthor" name="isAuthor"/>
                                <label classname="left-reg__isAuthor_text" for="isAuthor" htmlFor="mail">Хочу стать автором</label>
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