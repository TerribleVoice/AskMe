export const Footer = () => {
    return (
        <div className="container">
            <div className="footer__body">
              <div className="footer__left">
                <ul>
                  <li>Поддержка</li>
                  <li>Политика конфиденциальности</li>
                  <li>Пользовательское соглашение</li>
                </ul>
              </div>
              <div className="footer__right">
                <div className="footer__img">
                  <img src="img/profile/logo.png" alt="logo.png" />
                </div>
                <div className="footer__mail">dolores.chambers@example.com</div>
                <div className="footer__tel">+7 (903) 134-55-26</div>
              </div>
            </div>
            <img src="img/man.png" className="man" />
          </div>
    );
};
