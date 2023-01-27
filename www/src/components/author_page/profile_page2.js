//import './style.css';

export default function Profile_page2(props) {
    return (
        <body class="pp_body">
        <div class="pp_main">
            <div class="pp_main__container">
                <div class="pp_about">
                    <div class="pp_about__title">Об авторе</div>
                    <div class="pp_about__text">Разнообразный и богатый опыт сложившаяся структура организации влечет за собой процесс внедрения и модернизации соответствующий условий активизации.</div>
                </div>
                <div class="pp_post">
                    <div class="pp_post__title">
                        <div class="pp_post__text">Укрепление и развитие</div>
                        <div class="pp_post__date">29 января 2021, пт</div>
                    </div>
                    <div class="pp_post__img pp_blurred">
                        <img src="img/profile/photo2.jpg" alt="photo"></img>
                        <div class="pp_post__text2">
                            <span>Пост только для платных подписчиков</span>
                            <img src="img/profile/lock.svg" alt=""></img>
                        </div>
                    </div>
                </div>
                <aside class="pp_left">
                    <div class="pp_left__img">
                        <img src="img/profile/avatar3.jpg" alt="avatar"></img>
                    </div>
                    <div class="pp_left__body pp_body-left">
                        <div class="pp_body-left__nick">YOUNG77</div>
                        <div class="pp_body-left__job">Молодой и перспективный</div>
                        <div class="pp_body-left__subscribe">Подписаться</div>
                    </div>
                </aside>
                <aside class="pp_right">
                    <div class="pp_right__top pp_top-right">
                        <div class="pp_top-right__links">
                            <div class="pp_top-right__text">Ссылки</div>
                            <div class="pp_top-right__link pp_twitter">http://www.donware.com</div>
                            <div class="pp_top-right__link pp_youtube">http://www.zoomit.com</div>
                        </div>
                    </div>
                    <div class="pp_left__top pp_goal">
                        <div class="pp_goal__text">Цель</div>
                        <div class="pp_goal__progress">464 из 1500 рублей</div>
                        <div class="pp_goal__main">На значимые проблемы и крупные проекты</div>
                    </div>
                </aside>
            </div>
        </div>
    </body>
    )
};