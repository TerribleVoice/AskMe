import { GoBack } from "@/components/GoBack";
import { IUserCreatePost } from "@/models/IUserPosts";
import { userCreatePost } from "@/services/postUserPost";
import { useForm } from "react-hook-form";
import { useEffect, useState } from "react";
import { IUserSubscriptions } from "@/models/IUserSubscriptions";
import { getUserSubscriptions } from "@/services/getUserSubscriptions";
import { useParams, useNavigate } from "react-router-dom";

export const CreatePost = () => {
  const {
    register,
    handleSubmit,
    reset,
  } = useForm<IUserCreatePost>();
  const { LoginName } = useParams();
  const navigation = useNavigate();
  const [subscriptions, setSubscriptions] = useState<IUserSubscriptions[]>([]);
  const login = localStorage.getItem("login");
  // const [selectedImage, setSelectedImage] = useState<string | null>(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        if (LoginName !== undefined) {
          const data = await getUserSubscriptions(LoginName);
          console.log(data);
          setSubscriptions(data);
        } else {
          // navigation("/404");
        }
      } catch (error) {
        console.log(error);
      }
    };

    fetchData();
  }, [LoginName]);

  // const handleFileChange = (event: ChangeEvent<HTMLInputElement>) => {
  //   const file = event.target.files?.[0];
  //   if (file) {
  //     setSelectedImage(URL.createObjectURL(file));
  //   }
  //   return file;
  // };
  const onCreatePost = async (data: IUserCreatePost) => {
    try {
      // const formData = new FormData();
      // formData.append("title", data.title);
      // formData.append("content", data.content);
      // formData.append("price", data.price.toString());
      // formData.append("files", selectedImage!);
      // formData.append("subscriptionId", selectedSubscription);
      // console.log(formData);
      const response = await userCreatePost(data);
      console.log(response);
      if (response.status < 300) {
        console.log(response);
        navigation(`/${login}`);
      } else {
        reset();
        navigation(`/${login}`);
      }
    } catch (error) {
      navigation(`/${login}`);
    }
  };
  const [selectedSubscription, setSelectedSubscription] = useState<string>("");

  return (
    <div className="subscription_create_wrapper">
      <aside className="subscription_aside_left">
        <GoBack />
      </aside>
      <div className="subscription_create">
        <h2>Создание нового Поста</h2>
        <form
          className="subscription_form"
          onSubmit={handleSubmit(onCreatePost)}
        >
          <div className="create_post_subscriptions_wrapper">
            <p className="create_post_subscriptions_header">
              К КАКОЙ ПОДПИСКЕ ОТНОСИТСЯ ПОСТ?
            </p>
            {subscriptions?.map((subscription) => {
              const isChecked =
                selectedSubscription === subscription.id;
              return (
                <div
                  key={subscription.id}
                  className="create_post_subscriptions"
                >
                  <div className="subscription_checkbox">
                    <input
                      className="subscription_input_subscriptionId"
                      name="subscriptionId"
                      type="checkbox"
                      id={`subscription-${subscription.id}`}
                      checked={isChecked}
                      onChange={() =>
                        setSelectedSubscription(subscription.id.toString())
                      }
                    />
                    <div className="pp_subscription_name">
                      {subscription.name}
                    </div>
                    <div className="pp_subscription_price">
                      {subscription.price} рублей в месяц
                    </div>
                  </div>
                </div>
              );
            })}
          </div>
          <div className="subscription_input">
            <label htmlFor="title">Введите заголовок поста</label>
            <input
              className=""
              {...register("title", { required: true })}
              type="text"
              id="title"
              name="title"
            />
          </div>
          <div className="subscription_description">
            <label htmlFor="content">Описание поста</label>
            <textarea
              {...register("content", { required: false })}
              id="content"
              name="content"
            />
          </div>
          {/* <div className="file_post">
            <label htmlFor="image">Обложка</label>
            {selectedImage && (
              <div>
                <img id="image-preview" src={selectedImage} alt="Uploaded" />
              </div>
            )}
            <label className="custom_file_upload">
              <Controller
                control={control}
                name="files"
                render={({ field }) => (
                  <input
                    {...field}
                    onChange={(event) =>
                      field.onChange(handleFileChange(event))
                    }
                    type="file"
                    id="files"
                    value={undefined}
                  />
                )}
              />
              ВЫБРАТЬ ФАЙЛ
            </label>
            <label className="settings_caption" htmlFor="description">
              Рекомендуемый размер 240х150 рх
            </label>
          </div> */}
          {/* <div className="subscription_input">
            <label htmlFor="price">Стоимость поста</label>
            <input
              {...register("price", { required: true })}
              type="number"
              id="price"
              name="price"
              min={0}
              max={150000}
            />
          </div> */}
          <div className="left-reg__submit submit_form">
            <button type="submit">Создать</button>
          </div>
        </form>
      </div>
    </div>
  );
};
