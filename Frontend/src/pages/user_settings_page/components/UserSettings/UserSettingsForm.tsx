import { useForm } from "react-hook-form";

export const UserSettingsForm = () => {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm();
  const onSettingsSubmit = () => {

  }

  return (
    <form >
      <div className="left-reg__login">
        <label htmlFor="photo">Фотография</label>
        <input
          {...register("photo", { required: true })}
          type="file"
          id="photo"
        />
      </div>
      <div className="left-reg__login">
        <label htmlFor="login">Логин</label>
        <input {...register("login")} type="text" id="login" />
      </div>
      <div className="left-reg__login">
        <label htmlFor="email">Почта</label>
        <input {...register("email")} type="email" id="email" />
      </div>
      <div className="left-reg__submit">
        <button type="submit">Сохранить</button>
      </div>
    </form>
  );
};
