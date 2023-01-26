//import './style.css';

export default function Profile_page(props) {
    return (
        <body class="pp_body">
        <div class="pp_main">
            <div class="pp_main__container">
                <div class="pp_about">
                    <div class="pp_about__title">Об авторе</div>
                    <div class="pp_about__text">Душа моя озарена неземной радостью, как эти чудесные весенние утра, которыми я наслаждаюсь от всего сердца. Я совсем один и блаженствую в здешнем краю, словно созданном для таких, как я. Я так счастлив, мой друг, так упоен ощущением покоя, что искусство мое страдает от этого. Ни одного штриха не мог бы я сделать, а никогда не был таким большим художником, как в эти минуты.  </div>
                </div>
                <div class="pp_sort">
                    <div class="pp_sort__text">Сортировать</div>
                    <div class="pp_sort__arrow">
                        <img src="img/profile/dropdown.svg" alt="arrow"></img>
                    </div>
                </div>
                <div class="pp_post">
                    <div class="pp_post__title">
                        <div class="pp_post__text">Helping a local business reinvent itself</div>
                        <div class="pp_post__date">29 января 2021, пт</div>
                    </div>
                    <div class="pp_post__img pp_blurred">
                        <img src="img/profile/photo.jpg" alt="photo"></img>
                        <div class="pp_post__text2">
                            <span>Пост только для подписчиков</span>
                            <img src="img/profile/lock.svg" alt=""></img>
                        </div>
                    </div>
                </div>
                <aside class="pp_left">
                    <div class="pp_left__img">
                        <img src="img/profile/avatar1.jpg" alt="avatar"></img>
                    </div>
                    <div class="pp_left__body pp_body-left">
                        <div class="pp_body-left__nick">Автор 1</div>
                        <div class="pp_body-left__job">Род занятий</div>
                        <div class="pp_body-left__subscibers">0 подписчиков</div>
                        <div class="pp_body-left__money">0,00 руб/мес</div>
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
                        <div class="pp_goal__progress">30 из 100 рублей</div>
                        <div class="pp_goal__main">Ни штриха не мог бы я сделать, а никогда не был таким большим художником, как в эти минуты.</div>
                    </div>
                </aside>
            </div>
        </div>
    </body>
    )
};