import { IUserAuthentication } from "@/models/IUserAuthentication";
import "./AuthForm.css";
import { useForm } from "react-hook-form";
import { userAuthentication } from "@/services/userAuthentication";

export const AuthForm = () => {
  const {
    register,
    handleSubmit,
    reset,
    formState: { errors }, // нужен ли??
  } = useForm<IUserAuthentication>();

  const onAuthSubmit = (data: IUserAuthentication) => {
    console.log(data);
    const response = userAuthentication(data)
    console.log(response)
    reset()
  };

  return (
    <form onSubmit={handleSubmit(onAuthSubmit)} className="left-reg__form">
      <div className="left-reg__login">
        <label htmlFor="login">Логин</label>
        <input
          {...register("login", { required: true })}
          type="text"
          id="login"
        />
      </div>
      <div className="left-reg__password">
        <label htmlFor="password">Пароль</label>
        <input
          {...register("password", { required: true })}
          type="password"
          id="password"
        />
      </div>
      <div className="left-reg__submit">
        <button type="submit">Далее</button>
      </div>
    </form>
  );
};
