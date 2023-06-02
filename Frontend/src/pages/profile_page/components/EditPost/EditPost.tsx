import { GoBack } from "@/components/GoBack";
import {
  IUserEditSubscription,
  IUserSubscriptions,
} from "@/models/IUserSubscriptions";
import { userCreateSubscription } from "@/services/postUserCreateSubscription";
import { userEditSubscription } from "@/services/postUserEditSubscription";
import { useForm } from "react-hook-form";
import { useLocation, useNavigate, useParams } from "react-router-dom";
import { ProfilePage } from "../ProfilePage";
import { IUserPost, IUserUpdatePost } from "@/models/IUserPosts";
import { getUserSubscriptions } from "@/services/getUserSubscriptions";
import { useState, useEffect, useLayoutEffect } from "react";
import { postUserUpdatePost } from "@/services/postUserUpdatePost";
import { DeletePost } from "./DeletePost";
import { EditAttachPost } from "./EditAttachPost";

export const EditPost = () => {
  const {
    register,
    handleSubmit,
    reset,
    formState: { errors }, // нужен ли??
  } = useForm<IUserUpdatePost>();
  const { id } = useParams();
  const { state } = useLocation();
  const userPost: IUserPost = state;
  console.log(state);
  const navigation = useNavigate();
  const login = localStorage.getItem("login");

  const [subscriptions, setSubscriptions] = useState<IUserSubscriptions[]>([]);
  const [selectedSubscription, setSelectedSubscription] = useState<string>("");

  useLayoutEffect(() => {
    window.scrollTo(0, 0);
  }, []);
  
  useEffect(() => {
    const fetchData = async () => {
      try {
        if (login !== undefined) {
          const data = await getUserSubscriptions(login!);
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
  }, []);

  const onUpdatePost = async (data: IUserUpdatePost) => {
    try {
      console.log(data);
      const response = await postUserUpdatePost(data, id!);
      console.log(response);
      //   if (response.status < 300) {
      //     navigation(`/${login}`);
      //     console.log(response);
      //   } else {
      //     reset();
      //     alert("LSADJ:LASDJLA");
      //   }
    } catch (error) {
      console.error(error);
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
        <EditAttachPost postId={userPost.id} />
        <form
          className="subscription_form"
          onSubmit={handleSubmit(onUpdatePost)}
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
            <label htmlFor="name">Заголовок поста</label>
            <input
              placeholder={`${userPost.title}`}
              defaultValue={`${userPost.title}`}
              {...register("title")}
              type="text"
              id="title"
              name="title"
            />
          </div>
          <div className="subscription_description">
            <label htmlFor="content">Описание поста</label>
            <textarea
              placeholder={`${userPost.content}`}
              defaultValue={`${userPost.content}`}
              {...register("content", { required: true })}
              id="content"
              name="content"
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

