//import './style.css';

export const ProfilePage2 = () => {
  return (
    <body className="pp_body">
      <div className="pp_main">
        <div className="pp_main__container">
          <div className="pp_about">
            <div className="pp_about__title">Об авторе</div>
            <div className="pp_about__text">
              Разнообразный и богатый опыт сложившаяся структура организации
              влечет за собой процесс внедрения и модернизации соответствующий
              условий активизации.
            </div>
          </div>
          <div className="pp_post">
            <div className="pp_post__title">
              <div className="pp_post__text">Укрепление и развитие</div>
              <div className="pp_post__date">29 января 2021, пт</div>
            </div>
            <div className="pp_post__img pp_blurred">
              <img src="img/profile/photo2.jpg" alt="photo"></img>
              <div className="pp_post__text2">
                <span>Пост только для платных подписчиков</span>
                <img src="img/profile/lock.svg" alt=""></img>
              </div>
            </div>
          </div>
          <aside className="pp_left">
            <div className="pp_left__img">
              <img src="img/profile/avatar3.jpg" alt="avatar"></img>
            </div>
            <div className="pp_left__body pp_body-left">
              <div className="pp_body-left__nick">YOUNG77</div>
              <div className="pp_body-left__job">Молодой и перспективный</div>
              <div className="pp_body-left__subscribe">Подписаться</div>
            </div>
          </aside>
          <aside className="pp_right">
            <div className="pp_right__top pp_top-right">
              <div className="pp_top-right__links">
                <div className="pp_top-right__text">Ссылки</div>
                <div className="pp_top-right__link pp_twitter">
                  http://www.donware.com
                </div>
                <div className="pp_top-right__link pp_youtube">
                  http://www.zoomit.com
                </div>
              </div>
            </div>
            <div className="pp_left__top pp_goal">
              <div className="pp_goal__text">Цель</div>
              <div className="pp_goal__progress">464 из 1500 рублей</div>
              <div className="pp_goal__main">
                На значимые проблемы и крупные проекты
              </div>
            </div>
          </aside>
        </div>
      </div>
    </body>
  );
};
