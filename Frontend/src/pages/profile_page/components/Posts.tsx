import { IUserPost } from "@/models/IUserPosts";
import { zaglushkaPosts } from "@/pages/feed_page/components/zaglushkaPosts";
import { getUserPosts } from "@/services/getUserPosts";
import { useEffect, useState } from "react";
import { AiFillSetting } from "react-icons/ai";
import { useParams, useNavigate, Link } from "react-router-dom";
import { Modal } from "./Modal";
import { Attachment } from "./Attachment";
import ReactAudioPlayer from "react-audio-player";

export const Posts = () => {
  const { LoginName } = useParams();
  const urLogin = localStorage.getItem("login");
  const navigate = useNavigate();
  const [posts, setPosts] = useState<IUserPost[]>();

  useEffect(() => {
    try {
      const fetchData = async () => {
        if (LoginName !== undefined) {
          const data = await getUserPosts(LoginName);
          if (data === undefined) {
            setPosts(zaglushkaPosts); // заглушка
            // setPosts(data);
          } else {
            console.log(data);
            setPosts(data);
          }
        } else {
          navigate("/404");
        }
      };
      fetchData();
    } catch (error) {
      console.log(error);
    }
  }, [LoginName, navigate]);

  return (
    <div className="pp_posts_wrapper">
      {posts &&
        posts.map((post) => {
          const dateObj = new Date(post.createAt);
          const formattedDate = dateObj.toLocaleDateString("ru-RU", {
            year: "numeric",
            month: "long",
            day: "numeric",
            hour: "2-digit",
            minute: "2-digit",
          });
          return (
            <div key={post.id} className="pp_post">
              <div className="pp_post_head">
                {post.authorViewModel.profileImageUrl !== null ? (
                  <img
                    src={`${post.authorViewModel.profileImageUrl}`}
                    className="pp_post_profileAvatar"
                    alt="post_img"
                  />
                ) : (
                  <img
                    src={`/img/NoUserPhoto.svg`}
                    className="pp_post_profileAvatar"
                    alt="post_img"
                  />
                )}
                <div className="pp_post_profile">
                  <span className="pp_post_profileLogin">
                    {post.authorViewModel.login}
                  </span>
                  <span className="pp_post__date">{formattedDate}</span>
                </div>
                {LoginName === urLogin ? (
                  <Link
                    state={post}
                    className="pp_post__settings"
                    to={`/${LoginName}/edit_post/${post.id}`}
                  >
                    <img
                      style={{ width: "30px" }}
                      src="/img/post/Tochki3.svg"
                      alt="post_settings"
                    />
                  </Link>
                ) : (
                  <></>
                )}
              </div>
              <div className="pp_post__title">{post.title}</div>
              <div className="pp_post__text">{post.content}</div>
              {post.haveAccess && post.attachments.length <= 4 ? (
                <div className="pp_post__attach_wrapper">
                  {post.attachments !== undefined ? (
                    post.attachments
                      .slice(0, 4)
                      .map((a) => (
                        <Attachment
                          fileType={a!.fileType}
                          sourceUrl={a!.sourceUrl}
                        />
                      ))
                  ) : (
                    <></>
                  )}
                  <div className="pp_post__audio_wrapper">
                    {post.attachments !== undefined ? (
                      post.attachments.map((a) =>
                        a?.fileType === 3 ? (
                          <ReactAudioPlayer
                            className="pp_post__audio_attach"
                            src={a.sourceUrl}
                            controls
                          />
                        ) : (
                          <></>
                        )
                      )
                    ) : (
                      <></>
                    )}
                  </div>
                </div>
              ) : post.haveAccess && post.attachments.length >= 4 ? (
                <div className="pp_post__attach_wrapper">
                  {post.attachments !== undefined &&
                  post.attachments.map((a) => a) ? (
                    post.attachments
                      .map((a) => (
                        <Attachment
                          fileType={a!.fileType}
                          sourceUrl={a!.sourceUrl}
                        />
                      ))
                  ) : (
                    <></>
                  )}
                  <div className="pp_post__audio_wrapper">
                    {post.attachments !== undefined ? (
                      post.attachments.map((a) =>
                        a?.fileType === 3 ? (
                          <ReactAudioPlayer
                            className="pp_post__audio_attach"
                            src={a.sourceUrl}
                            controls
                          />
                        ) : (
                          <></>
                        )
                      )
                    ) : (
                      <></>
                    )}
                  </div>
                </div>
              ) : (
                <div className="pp_post__img_wrapper pp_blurred">
                  {/* {const att = post.attachments.map((a) => a?.fileType == 0 ? a.sourceUrl : "/img/NoUserPhoto.svg")} */}
                  <img
                    className="pp_post__img"
                    src={"/img/NoUserPhoto.svg"}
                    alt="."
                  />
                  <div className="pp_post__text2">
                    <p>Пост только для платных подписчиков</p>
                  </div>
                </div>
              )}
            </div>
          );
        })}
    </div>
  );
};
