import { IUserRegistration } from "@/models/IUserRegistration";
import "./RegForm.css";
import { useForm } from "react-hook-form";
import { userRegistration } from "@/services/userRegistration";

export const RegForm = () => {
  const {
    register,
    handleSubmit,
    reset,
    formState: { errors }, // нужен ли??
  } = useForm<IUserRegistration>();

  const onRegSubmit = (data: IUserRegistration) => {
    console.log(data);
    const response = userRegistration(data);
    console.log(response)
    reset()
  };

  return (
    <form onSubmit={handleSubmit(onRegSubmit)} className="left-reg__form">
      <div className="left-reg__mail">
        <label htmlFor="mail">Электронная почта</label>
        <input
          {...register("email", { required: true })}
          type="email"
        />
      </div>
      <div className="left-reg__login">
        <label htmlFor="login">Логин</label>
        <input
          {...register("login", { required: true })}
          id="login"
          type="text"
        />
      </div>
      <div className="left-reg__password">
        <label htmlFor="password">Пароль</label>
        <input
          {...register("password", { required: true })}
          id="password"
          type="password"
        />
      </div>
      <div className="left-reg__isAuthor">
        <input {...register("isAuthor")} type="checkbox" id="isAuthor" />
        <label className="left-reg__isAuthor_text" htmlFor="isAuthor">
          Хочу стать автором
        </label>
      </div>
      <div className="left-reg__submit">
        <button type="submit">Далее</button>
      </div>
    </form>
  );
};
