export const Footer: React.FC = () => {
  return (
    <div className="footer">
      <div className="container">
        <div className="footer__body">
          <div className="footer__left">
            <ul>
              <li className="footer__link">Поддержка</li>
              <li className="footer__link">Политика конфиденциальности</li>
              <li className="footer__link">Пользовательское соглашение</li>
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
        <img src="img/man.png" className="man" alt="man.png" />
      </div>
    </div>
  );
};
