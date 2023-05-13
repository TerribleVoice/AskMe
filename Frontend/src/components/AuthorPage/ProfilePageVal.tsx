import { IUserProfilePage } from "@/models/IUserProfilePage";
import { getUserProfilePage } from "@/services/getUserProfilePage";
import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";

const zaglushka: IUserProfilePage = {
  login: "Shaman",
  isAuthor: false,
  description: "eti rolexu mne muzh kupil",
  status: "eto frendly faer ogon' po svoim",
  links: ["http://www.banda.na", "http://www.ogorgor.od"],
  posts: [
    {
      id: "empty",
      content: "view content",
      price: 42,
      createAt: "01.01.21",
      haveAccess: false,
      subscriptionName: "Krip Uok",
    },
  ],
};

export const ProfilePageVal = () => {
  const { LoginName } = useParams();
  const navigate = useNavigate();
  const [profileData, setProfileData] = useState<IUserProfilePage>();

  useEffect(() => {
    try {
      const fetchData = async () => {
        if (LoginName !== undefined) {
          const data = await getUserProfilePage(LoginName);
          if (data === undefined) {
            setProfileData(zaglushka);
          } else {
            setProfileData(data);
          }
        } else {
          navigate("/404")
        }
      };
      fetchData();
    } catch (error) {
      console.log(error);
    } finally {
      setProfileData(zaglushka);
    }
  }, [LoginName]);

  return (
    <div className="container">
      <div className="pp_main">
        <div className="pp_main__container">
          <div className="pp_about">
            <div className="pp_about__title">Об авторе</div>
            <div className="pp_about__text">
              {profileData?.description ? profileData.description : ""}
            </div>
          </div>
          <div className="pp_sort">
            <div className="pp_sort__text">Сортировать</div>
            <div className="pp_sort__arrow">
              <img src="img/profile/dropdown.svg" alt="arrow"></img>
            </div>
          </div>
          {profileData?.posts?.map((post) => {
            return (
              <div key={post.id} className="pp_post">
                <div className="pp_post__title">
                  <div className="pp_post__text">
                    {/* Здесь нужно поле Оглавление */}
                    Helping a local business reinvent itself
                  </div>
                  <div className="pp_post__date">{post.createAt}</div>
                </div>
                {post.haveAccess ? (
                  <div className="pp_post__img">
                    <img src="img/profile/photo.jpg" alt="profile"></img>
                    <div className="pp_post__text2">{post.content}</div>
                  </div>
                ) : (
                  <div className="pp_post__img pp_blurred">
                    <img src="img/profile/photo.jpg" alt="profile"></img>
                    <div className="pp_post__text2">
                      <p>Пост только для платных подписчиков</p>
                      <img src="img/profile/lock.svg" alt="lock.svg"></img>
                      <p>{post.subscriptionName}</p>
                      <p>{`${post.price}$$`}</p>
                    </div>
                  </div>
                )}
              </div>
            );
          })}
          <aside className="pp_left">
            <div className="pp_left__img">
              <img src="img/profile/avatar1.jpg" alt="avatar"></img>
            </div>
            <div className="pp_left__body pp_body-left">
              <div className="pp_body-left__nick">{profileData?.login}</div>
              <div className="pp_body-left__job">{profileData?.status}</div>
              <div className="pp_body-left__subscribe">Подписаться</div>
            </div>
          </aside>
          <aside className="pp_right">
            <div className="pp_right__top pp_top-right">
              <ul className="pp_top-right__links">
                <p className="pp_top-right__text">Ссылки</p>
                {profileData?.links?.map((link) => (
                  <li key={link} className="pp_top-right__link">
                    {link}
                  </li>
                ))}
              </ul>
            </div>
          </aside>
        </div>
      </div>
    </div>
  );
};
