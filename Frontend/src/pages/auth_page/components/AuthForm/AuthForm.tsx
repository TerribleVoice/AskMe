import { IUserAuthentication } from "@/models/IUserAuthentication";
import "./AuthForm.css";
import { useForm } from "react-hook-form";
import { userAuthentication } from "@/services/postUserAuthentication";
import { useNavigate } from "react-router-dom";

export const AuthForm = () => {
  const {
    register,
    handleSubmit,
    reset,
    formState: { errors }, // нужен ли??
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
        document.location.reload();
      } else {
        reset();
        alert("LSADJ:LASDJLA");
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
    </>
  );
};
