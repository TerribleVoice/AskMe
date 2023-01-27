//import './style.css';

export default function Profile_page1(props) {
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
                        <div class="pp_post__text">Разнообразный и богатый опыт</div>
                        <div class="pp_post__date">29 января 2021, пт</div>
                    </div>
                    <div class="pp_post__img pp_blurred">
                        <img src="img/profile/photo1.jpg" alt="photo"></img>
                        <div class="pp_post__text2">
                            <span>Пост только для платных подписчиков</span>
                            <img src="img/profile/lock.svg" alt=""></img>
                        </div>
                    </div>
                </div><br/><br/>
                <div class="pp_post">
                    <div class="pp_post__title">
                        <div class="pp_post__text">Разнообразный и богатый опыт</div>
                        <div class="pp_post__date">29 января 2021, пт</div>
                    </div>
                    <div class="pp_post__img pp_blurred">
                        <img src="img/profile/photo1.jpg" alt="photo"></img>
                        <div class="pp_post__text2">
                            <span>Пост только для платных подписчиков</span>
                            <img src="img/profile/lock.svg" alt=""></img>
                        </div>
                    </div>
                </div>
                <aside class="pp_left">
                    <div class="pp_left__img">
                        <img src="img/profile/avatar2.jpg" alt="avatar"></img>
                    </div>
                    <div class="pp_left__body pp_body-left">
                        <div class="pp_body-left__nick">ObabMaster</div>
                        <div class="pp_body-left__job">Лучший в своём деле</div>
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
                        <div class="pp_goal__progress">234 из 1000 рублей</div>
                        <div class="pp_goal__main">На идейные соображения высшего порядка</div>
                    </div>
                </aside>
            </div>
        </div>
    </body>
    )
};