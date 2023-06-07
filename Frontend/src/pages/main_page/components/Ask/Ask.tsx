import { Link } from "react-router-dom";

export const Ask = () => {
  const login = localStorage.getItem("login");
  return (
    <div className="container">
      <div className="ask">
        <div className="left">
          <div className="left__title">
            <img src="img/AskMe.png" alt="AskMe.png" />
          </div>
          <div className="left__text">Ваше творчество - ваш заработок </div>
          {login ? (
            <div className="left__text">Добро пожаловать</div>
          ) : (
            <Link to="/auth">
              <div className="left__btn">Регистрация</div>
            </Link>
          )}
        </div>
        <div className="right">
          <img src="img/face.png" alt="Face.png" />
        </div>
      </div>
    </div>
  );
};
