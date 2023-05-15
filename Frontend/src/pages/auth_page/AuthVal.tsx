import { useState } from "react";
import "./Auth.css";

import { AuthForm } from "@/pages/auth_page/components/AuthForm/AuthForm";
import { RegForm } from "@/pages/auth_page/components/RegForm/RegForm";

export const AuthVal = () => {
  const [authReg, setAuthReg] = useState(false);
  const handleSwitchAuthReg = () => {
    setAuthReg(!authReg);
  };
  return (
    <div className="wrapper">
      <div className="main">
        <img className="main__angel" src="angel.png" alt="angel.png" />
        <div className="reg">
          <div className="reg__left left-reg">
            <div className="left-reg__choose">
              <div
                className={`left-reg__registation ${
                  authReg ? "" : "active-btn"
                }`}
                onClick={handleSwitchAuthReg}
              >
                Регистрация
              </div>
              <div
                className={`left-reg__auth ${authReg ? "active-btn" : ""}`}
                onClick={handleSwitchAuthReg}
              >
                Авторизация
              </div>
            </div>
            <div className="left-reg__welcome">Добро пожаловать</div>
            {authReg ? <AuthForm /> : <RegForm />}
          </div>
          <div className="reg__right">
            <img src="woman.jpg" alt="woman.jpg" />
          </div>
        </div>
      </div>
    </div>
  );
};
