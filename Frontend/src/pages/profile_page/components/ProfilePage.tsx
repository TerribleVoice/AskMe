import { IUserProfilePage } from "@/models/IUserProfilePage";
import { getUserProfilePage } from "@/services/getUserProfilePage";
import { useEffect, useState } from "react";
import { Link, useNavigate, useParams } from "react-router-dom";
import { Posts } from "./Posts";
import { Subscriptions } from "./Subscriptions";

const zaglushka: IUserProfilePage = {
  login: "Shaman",
  description: "eti rolexu mne muzh kupil",
  profileImageUrl: "asdasdasda",
  links: "asdasdasdasdasda",
  // status: "eto frendly faer ogon' po svoim",
  // links: ["http://www.banda.na", "http://www.ogorgor.od"],
  // posts: [
  //   {
  //     id: "empty",
  //     content: "view content",
  //     price: 42,
  //     createAt: "01.01.21",
  //     haveAccess: false,
  //     subscriptionName: "Krip Uok",
  //   },
  // ],
};

export const ProfilePage = () => {
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
            console.log(data);
            setProfileData(data);
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

  return (
    <>
      <div className="pp_about">
        <div className="pp_about__title">
          <span>Об авторе</span>
          <span></span>
        </div>
        <div className="pp_about__text">
          {profileData?.description ? profileData.description : ""}
        </div>
      </div>
      <Posts />
      <aside className="pp_left">
        <div className="pp_left__img">
          <img className="pp_left__avatar" src={image} alt="ava" />
          {!image && (
            <img
              className="pp_left__avatar"
              src="img/NoUserPhoto.svg"
              alt="ava"
            />
          )}
        </div>
        <div className="pp_left__body pp_body-left">
          <div className="pp_body-left__nick">{LoginName}</div>
          {/* <div className="pp_body-left__job">{profileData?.status}</div> */}
        </div>
        <Link to={"create_post"} className="pp_body-create_post">
          СОЗДАТЬ ПУБЛИКАЦИЮ
        </Link>
      </aside>
      <aside className="pp_right">
        <div className="pp_right__top pp_top-right">
          <ul className="pp_top-right__links">
            <p className="pp_top-right__text">Ссылки</p>
            {/* {profileData?.links?.map((link) => (
              <li key={link} className="pp_top-right__link">
                {link}
              </li>
            ))} */}
          </ul>
        </div>
        <Subscriptions />
      </aside>
    </>
  );
};
