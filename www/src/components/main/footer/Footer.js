export default function Footer(props) {
    return (
        <div className="container">
            <div className="footer__body">
              <div className="footer__left">
                <ul>
                  <li>Exercitation</li>
                  <li>Amet</li>
                  <li>Velit offician</li>
                  <li>Edeserunt ullamco</li>
                </ul>
              </div>
              <div className="footer__right">
                <div className="footer__img">
                  <img src="img/AskMe.png" alt />
                </div>
                <div className="footer__mail">dolores.chambers@example.com</div>
                <div className="footer__tel">+7 (903) 134-55-26</div>
              </div>
            </div>
            <img src="img/man.png" className="man" />
          </div>
    );
};
