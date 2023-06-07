import { GoBack } from "@/components/GoBack";
import { IUserCreatePost } from "@/models/IUserPosts";
import { userCreatePost } from "@/services/postUserPost";
import { Controller, useForm } from "react-hook-form";
import { ChangeEvent, useEffect, useState } from "react";
import { IUserSubscriptions } from "@/models/IUserSubscriptions";
import { getUserSubscriptions } from "@/services/getUserSubscriptions";
import { useParams, useNavigate } from "react-router-dom";

export const CreatePost = () => {
  const {
    register,
    handleSubmit,
    reset,
    control,
    formState: { errors },
  } = useForm<IUserCreatePost>();
  const { LoginName } = useParams();
  const navigation = useNavigate();
  const [subscriptions, setSubscriptions] = useState<IUserSubscriptions[]>([]);
  const [selectedImage, setSelectedImage] = useState<string[]>([]);
  const login = localStorage.getItem("login");
  const [attachments, setAttachments] = useState<FileList>([] as unknown as FileList)

  useEffect(() => {
    const fetchData = async () => {
      try {
        if (LoginName !== undefined) {
          const data = await getUserSubscriptions(LoginName);
          // console.log(data);
          setSubscriptions(data);
        } else {
          navigation("/404");
        }
      } catch (error) {
        console.log(error);
      }
    };

    fetchData();
  }, []);

  const handleFileChange = (event: ChangeEvent<HTMLInputElement>) => {
    const files = event.target.files;
    // console.log(files);
    if (files) {
      const fileURLs = Array.from(files).map((file) =>
        URL.createObjectURL(file)
      );
      setSelectedImage((prevImages) => [...prevImages, ...fileURLs]);
      const dataTransfer = new DataTransfer();
      Array.from(attachments).forEach((file) =>
        dataTransfer.items.add(file as File)
      );
      Array.from(files).forEach((file) => dataTransfer.items.add(file));
      const newFileList = dataTransfer.files;
      setAttachments(newFileList);
      // console.log(newFileList)
      // console.log(attachments)
      return newFileList;
    }
  };
  const onCreatePost = async (data: IUserCreatePost) => {
    try {
      // console.log(data);
      console.log(data)
      if (!data.attachments) {
        data.attachments = [] as unknown as FileList;
      }
      const formData = new FormData();
      formData.append("Title", data.Title);
      formData.append("Content", data.Content);
      formData.append("SubscriptionId", selectedSubscription);
      if (attachments) {
        Array.from(data.attachments).forEach((file, index) => formData.append("attachments", file, `${index}`));
      }
      // formData.append("attachments", data.attachments[0], "chris1.jpg");
      // formData.append("attachments", data.attachments[1], "chris2.jpg");
      // formData.append("attachments", data.attachments, "files");
      console.log(formData);
      const response = await userCreatePost(formData);
      console.log(response);
      if (response.status < 300) {
        navigation(`/${login}`);
        console.log(response);
        navigation(`/${login}`);
      } else {
        reset();
        navigation(`/${login}`);
      }
    } catch (error) {
      console.log(error)
      // navigation(`/${login}`);
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
              const isChecked = selectedSubscription === subscription.id;
              return (
                <div
                  key={subscription.id}
                  className="create_post_subscriptions"
                >
                  <div className="subscription_checkbox">
                    <input
                      {...register("SubscriptionId", { required: true })}
                      className="subscription_input_subscriptionId"
                      name="SubscriptionId"
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
          <div className="file_post">
            <label htmlFor="image">Обложка</label>
            {/* {selectedImage && (
              <div>
                <img id="image-preview" src={selectedImage} alt="Uploaded" />
              </div>
            )} */}
            {selectedImage.map((si) => (
              <img key={si} id="image-preview" src={si} alt="Uploaded" />
            ))}
            <label className="custom_file_upload">
              <Controller
                control={control}
                name="attachments"
                render={({ field }) => (
                  <input
                    {...field}
                    onChange={(event) =>
                      field.onChange(handleFileChange(event))
                    }
                    type="file"
                    id="attachments"
                    value={[]}
                  />
                )}
              />
              ВЫБРАТЬ ФАЙЛ
            </label>
            {/* <label className="settings_caption" htmlFor="description">
              Рекомендуемый размер 240х150 рх
            </label> */}
          </div>
          <div className="subscription_input">
            <label htmlFor="Title">Введите заголовок поста</label>
            <input
              className=""
              {...register("Title", { required: false })}
              type="text"
              id="Title"
              name="Title"
            />
          </div>
          <div className="subscription_description">
            <label htmlFor="Content">Описание поста</label>
            <textarea
              {...register("Content", { required: false })}
              id="Content"
              name="Content"
            />
          </div>
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
