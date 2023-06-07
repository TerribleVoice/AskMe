import { GoBack } from "@/components/GoBack";
import { IUserSubscriptions } from "@/models/IUserSubscriptions";
import { Controller, useForm } from "react-hook-form";
import { useLocation, useNavigate, useParams } from "react-router-dom";
import { IUserPost, IUserUpdatePost } from "@/models/IUserPosts";
import { getUserSubscriptions } from "@/services/getUserSubscriptions";
import { useState, useEffect, useLayoutEffect, ChangeEvent } from "react";
import { postUserUpdatePost } from "@/services/postUserUpdatePost";
import { DeletePost } from "./DeletePost";

export const EditPost = () => {
  const {
    register,
    handleSubmit,
    reset,
    control,
    formState: { errors },
  } = useForm<IUserUpdatePost>();
  const { id } = useParams();
  const { state } = useLocation();
  const userPost: IUserPost = state;
  console.log(state);
  const navigation = useNavigate();
  const login = localStorage.getItem("login");

  const [subscriptions, setSubscriptions] = useState<IUserSubscriptions[]>([]);
  const [selectedSubscription, setSelectedSubscription] = useState<string>("");
  const [selectedImage, setSelectedImage] = useState<string[]>([]);
  const [attachments, setAttachments] = useState<FileList | null>(null);

  useLayoutEffect(() => {
    window.scrollTo(0, 0);
  }, []);

  useEffect(() => {
    const stateUrls = userPost.attachments.map((a) => a!.sourceUrl);
    setSelectedImage(stateUrls);

    const fetchData = async () => {
      try {
        if (login !== null) {
          const data = await getUserSubscriptions(login);
          console.log(data);
          setSubscriptions(data);
        } else {
          navigation("/404");
        }
      } catch (error) {
        console.log(error);
      }
    };

    fetchData();
  }, [login, navigation, userPost.attachments]);

  const onUpdatePost = async (data: IUserUpdatePost) => {
    try {
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
      const response = await postUserUpdatePost(formData, id!);
      console.log(response);
      navigation(`/${login}`);
    } catch (error) {
      console.error(error);
    }
  };

  const handleFileChange = (event: ChangeEvent<HTMLInputElement>): void => {
    const files = event.target.files;
    if (files) {
      const fileURLs = Array.from(files).map((file) =>
        URL.createObjectURL(file)
      );
      setSelectedImage((prevImages) => [...prevImages, ...fileURLs]);
      const dataTransfer = new DataTransfer();
      if (attachments) {
        Array.from(attachments).forEach((file) =>
          dataTransfer.items.add(file as File)
        );
      }
      Array.from(files).forEach((file) => dataTransfer.items.add(file));
      const newFileList = dataTransfer.files;
      setAttachments(newFileList);
    }
  };

  return (
    <div className="subscription_create_wrapper">
      <aside className="subscription_aside_left">
        <GoBack />
      </aside>
      <div className="subscription_create">
        <DeletePost />
        <h2>Редактирование поста</h2>
        <form
          className="subscription_form"
          onSubmit={handleSubmit(onUpdatePost)}
        >
          <div className="subscription_image">
            <label htmlFor="image">Обложка поста</label>
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
                    onChange={(event) => handleFileChange(event)}
                    type="file"
                    id="attachments"
                    value={[]}
                  />
                )}
              />
              ВЫБРАТЬ ФАЙЛ
            </label>
          </div>
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
          <div className="subscription_input">
            <label htmlFor="Title">Заголовок поста</label>
            <input
              placeholder={`${userPost.title}`}
              defaultValue={`${userPost.title}`}
              {...register("Title")}
              type="text"
              id="Title"
              name="Title"
            />
          </div>
          <div className="subscription_description">
            <label htmlFor="Content">Описание поста</label>
            <textarea
              placeholder={`${userPost.content}`}
              defaultValue={`${userPost.content}`}
              {...register("Content", { required: true })}
              id="Content"
              name="Content"
            />
          </div>
          <div className="left-reg__submit submit_form">
            <button type="submit">Редактировать</button>
          </div>
        </form>
      </div>
    </div>
  );
};
