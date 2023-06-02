import { IUserProfilePage } from "@/models/IUserProfilePage";
import { getUserProfilePage } from "@/services/getUserProfilePage";
import { useEffect, useState } from "react";
import { Link, useNavigate, useParams } from "react-router-dom";
import { Posts } from "./Posts";
import { Subscriptions } from "./Subscriptions";
import { getUserSubscriptions } from "@/services/getUserSubscriptions";
import { IUserSubscriptions } from "@/models/IUserSubscriptions";

const zaglushka: IUserProfilePage = {
  login: "Login1",
  description:
    "Description1 Description1 Description1 Description1 Description1 Description1 Description1 Description1 Description1 Description1 ",
  profileImageUrl: "/img/NoUserPhoto.svg",
  links: "https://link1.com",
};

export const ProfilePage = () => {
  const { LoginName } = useParams();
  const yourLoginName = localStorage.getItem("login");
  const navigate = useNavigate();
  const [profileData, setProfileData] = useState<
    IUserProfilePage | undefined
  >();
  const [subscriptions, setSubscriptions] = useState<IUserSubscriptions[]>([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        if (LoginName !== undefined) {
          const data = await getUserSubscriptions(LoginName);
          console.log(data);
          setSubscriptions(data);
        } else {
          navigate("/404");
        }
      } catch (error) {
        console.log(error);
      }
    };
    fetchData();
  }, [LoginName]);

  useEffect(() => {
    try {
      const fetchData = async () => {
        if (LoginName !== undefined) {
          const data = await getUserProfilePage(LoginName);
          if (data === undefined) {
            setProfileData(zaglushka);
          } else {
            console.log(data);
            setProfileData(data);
            if (
              (localStorage.getItem("description") === null &&
                localStorage.getItem("links") === null) ||
              localStorage.getItem("login") !== LoginName
            ) {
              localStorage.setItem("description", data.description);
              localStorage.setItem("links", data.links);
            }
          }
        } else {
          navigate("/404");
        }
      };
      fetchData();
    } catch (error) {
      console.log(error);
    }
  }, [LoginName]);

  const image = profileData?.profileImageUrl;
  const links = profileData?.links

  console.log(links)
  return (
    <>
      <div className="mobile_pp_avatar">
        <div className="pp_left__img">
          {profileData?.profileImageUrl !== null ? (
            <img className="pp_left__avatar" src={`${image}`} alt="avatar" />
          ) : (
            <img
              className="pp_left__avatar"
              src={`img/NoUserPhoto.svg`}
              alt="noava"
            />
          )}
        </div>
        <div className="pp_left__body pp_body-left">
          <div className="pp_body-left__nick">{LoginName}</div>
        </div>
        {LoginName === yourLoginName && subscriptions.length !== 0 ? (
          <Link to="create_post" className="pp_body-create_post">
            СОЗДАТЬ ПУБЛИКАЦИЮ
          </Link>
        ) : LoginName === yourLoginName && subscriptions.length === 0 ? (
          <>
            <div className="unactive">
              <span className="unactive_notif">
                Опубликовать пост можно если у вас создан хотя бы один уровень
                подписки
              </span>
            </div>
            <Link
              to="create_subscription"
              onClick={() => navigate(`/${LoginName}`)}
              className="pp_body-create_subscr"
              style={{
                marginTop: "10px",
                marginLeft: "10px",
                marginRight: "10px",
              }}
            >
              ДОБАВИТЬ ПОДПИСКУ
            </Link>
          </>
        ) : null}
      </div>
      <div className="pp_about">
        <div className="pp_about__title">
          <span>Об авторе</span>
          <span></span>
        </div>
        <div className="pp_about__text">
          {profileData?.description ? profileData.description : ""}
        </div>
      </div>
      <div className="pp_mobile_links">
        <p className="pp_top-right__text">Ссылки</p>
        <ul className="pp_top-right__links">
          {links === null || links === undefined || links === "null"
            ? null
            : links.split("\n")?.map((l) => (
                <Link to={l} className="pp_links">
                  {l}
                </Link>
              ))}
        </ul>
      </div>
      <div className="pp_mobile_subs">
        <Subscriptions subs={subscriptions} />
      </div>
      <div className="pp_postswrap">
        <Posts />
      </div>
      <aside className="pp_left">
        <div className="pp_left__img">
          {profileData?.profileImageUrl !== null ? (
            <img className="pp_left__avatar" src={`${image}`} alt="avatar" />
          ) : (
            <img
              className="pp_left__avatar"
              src={`img/NoUserPhoto.svg`}
              alt="noava"
            />
          )}
        </div>
        <div className="pp_left__body pp_body-left">
          <div className="pp_body-left__nick">{LoginName}</div>
        </div>
        {LoginName === yourLoginName && subscriptions.length !== 0 ? (
          <Link to="create_post" className="pp_body-create_post">
            СОЗДАТЬ ПУБЛИКАЦИЮ
          </Link>
        ) : LoginName === yourLoginName && subscriptions.length === 0 ? (
          <>
            <div className="unactive">
              <span className="unactive_notif">
                Опубликовать пост можно если у вас создан хотя бы один уровень
                подписки
              </span>
            </div>
            <Link
              to="create_subscription"
              onClick={() => navigate(`/${LoginName}`)}
              className="pp_body-create_subscr"
              style={{
                marginTop: "10px",
                marginLeft: "10px",
                marginRight: "10px",
              }}
            >
              ДОБАВИТЬ ПОДПИСКУ
            </Link>
          </>
        ) : null}
      </aside>
      <aside className="pp_right">
        <div className="pp_right__top pp_top-right">
          <p className="pp_top-right__text">Ссылки</p>
          <ul className="pp_top-right__links">
            {links === null || links === undefined || links === "null"
              ? null
              : links.split("\r\n")?.map((l) => (
                  <Link to={l} className="pp_links">
                    {l}
                  </Link>
                ))}
          </ul>
        </div>
        <Subscriptions subs={subscriptions} />
      </aside>
    </>
  );
};
