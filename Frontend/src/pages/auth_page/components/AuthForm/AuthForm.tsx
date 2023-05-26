import "./AuthForm.css"
import { useForm } from "react-hook-form";
import { useNavigate } from "react-router-dom";
import { IUserAuthentication } from "@/models/IUserAuthentication";
import { userAuthentication } from "@/services/postUserAuthentication";

export const AuthForm: React.FC = () => {
  const {
    register,
    handleSubmit,
    reset,
    formState: { errors },
  } = useForm<IUserAuthentication>();
  const navigate = useNavigate();

  const onAuthSubmit = async (data: IUserAuthentication) => {
    try {
      console.log(data);
      const response = await userAuthentication(data);
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
      <div className="left-reg__text">Введите логин и пароль</div>
      <form onSubmit={handleSubmit(onAuthSubmit)} className="left-reg__form">
        <div className="left-reg__login">
          <label htmlFor="login">Логин</label>
          <input {...register("login", { required: true })} type="text" id="login" />
        </div>
        <div className="left-reg__password">
          <label htmlFor="password">Пароль</label>
          <input {...register("password", { required: true })} type="password" id="password" />
        </div>
        <div className="left-reg__submit">
          <button type="submit">Далее</button>
        </div>
      </form>
    </>
  );
};
