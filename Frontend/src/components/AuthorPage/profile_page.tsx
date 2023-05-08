//import './style.css';

export const Profile_page = () => {
  return (
    <body className="pp_body">
      <div className="pp_main">
        <div className="pp_main__container">
          <div className="pp_about">
            <div className="pp_about__title">Об авторе</div>
            <div className="pp_about__text">
              Душа моя озарена неземной радостью, как эти чудесные весенние
              утра, которыми я наслаждаюсь от всего сердца. Я совсем один и
              блаженствую в здешнем краю, словно созданном для таких, как я. Я
              так счастлив, мой друг, так упоен ощущением покоя, что искусство
              мое страдает от этого. Ни одного штриха не мог бы я сделать, а
              никогда не был таким большим художником, как в эти минуты.{" "}
            </div>
          </div>
          <div className="pp_sort">
            <div className="pp_sort__text">Сортировать</div>
            <div className="pp_sort__arrow">
              <img src="img/profile/dropdown.svg" alt="arrow"></img>
            </div>
          </div>
          <div className="pp_post">
            <div className="pp_post__title">
              <div className="pp_post__text">
                Helping a local business reinvent itself
              </div>
              <div className="pp_post__date">29 января 2021, пт</div>
            </div>
            <div className="pp_post__img pp_blurred">
              <img src="img/profile/photo.jpg" alt="photo"></img>
              <div className="pp_post__text2">
                <span>Пост только для платных подписчиков</span>
                <img src="img/profile/lock.svg" alt=""></img>
              </div>
            </div>
          </div>
          <aside className="pp_left">
            <div className="pp_left__img">
              <img src="img/profile/avatar1.jpg" alt="avatar"></img>
            </div>
            <div className="pp_left__body pp_body-left">
              <div className="pp_body-left__nick">TheOnlyOne1</div>
              <div className="pp_body-left__job">Один такой</div>
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
              <div className="pp_goal__progress">30 из 100 рублей</div>
              <div className="pp_goal__main">
                Ни штриха не мог бы я сделать, а никогда не был таким большим
                художником, как в эти минуты.
              </div>
            </div>
          </aside>
        </div>
      </div>
    </body>
  );
};
