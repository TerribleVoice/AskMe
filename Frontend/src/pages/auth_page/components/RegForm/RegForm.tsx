import React from "react";
import "./RegForm.css"
import { useForm } from "react-hook-form";
import { useNavigate } from "react-router-dom";
import { IUserRegistration } from "@/models/IUserRegistration";
import { userRegistration } from "@/services/postUserRegistration";

export const RegForm: React.FC = () => {
  const {
    register,
    handleSubmit,
    reset,
    formState: { errors },
  } = useForm<IUserRegistration>();
  const navigate = useNavigate();

  const onRegSubmit = async (data: IUserRegistration) => {
    try {
      console.log(data);
      const response = await userRegistration(data);
      console.log(response);
      if (response.status < 300) {
        localStorage.setItem("login", data.login);
        navigate("/", { replace: true });
      } else {
        reset();
      }
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <>
      <div className="left-reg__text">
        Введите адрес электронной почты, придумайте логин и пароль
      </div>
      <form onSubmit={handleSubmit(onRegSubmit)} className="left-reg__form">
        <div className="left-reg__mail">
          <label htmlFor="mail">Электронная почта</label>
          <input {...register("email", { required: true })} type="email" />
        </div>
        <div className="left-reg__login">
          <label htmlFor="login">Логин</label>
          <input {...register("login", { required: true })} id="login" type="text" />
        </div>
        <div className="left-reg__password">
          <label htmlFor="password">Пароль</label>
          <input {...register("password", { required: true })} id="password" type="password" />
        </div>
        <div className="left-reg__submit">
          <button type="submit">Далее</button>
        </div>
      </form>
    </>
  );
};
