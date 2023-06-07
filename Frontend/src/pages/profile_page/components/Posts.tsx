import { IUserPost } from "@/models/IUserPosts";
import { zaglushkaPosts } from "@/pages/feed_page/components/zaglushkaPosts";
import { getUserPosts } from "@/services/getUserPosts";
import { useEffect, useState } from "react";
import { AiFillSetting } from "react-icons/ai";
import { useParams, useNavigate, Link } from "react-router-dom";
import Modal from "@/components/Modal";

export const Posts = () => {
  const [modalActive, setModalActive] = useState(false);
  const { LoginName } = useParams();
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
              <div
                style={{
                  display: "flex",
                  flexDirection: "row",
                  alignItems: "center",
                  backgroundColor: "#181818",
                }}
              >
                {post.authorViewModel.profileImageUrl !== null ? (
                  <img
                    src={`${post.authorViewModel.profileImageUrl}`}
                    style={{ width: "50px", margin: "20px" }}
                    alt="post_img"
                  />
                ) : (
                  <img
                    src={`/img/NoUserPhoto.svg`}
                    style={{ width: "50px", margin: "20px" }}
                    alt="post_img"
                  />
                )}
                <span style={{ fontSize: "20px" }}>
                  {post.authorViewModel.login}
                </span>
                <div className="pp_post__date">
                  {formattedDate}
                </div>
                {localStorage.getItem("login") === post.authorViewModel.login ?
                <div className="pp_post_editicon">
                <Link state={post} to={`/${LoginName}/edit_post/${post.id}`}>
                  <AiFillSetting />
                </Link>
                </div>
                 : null}
              </div>
              <div
                className="pp_post__text"
                style={{ backgroundColor: "#181818" }}
              >
                <div className="pp_post__title">{post.title}</div>
                {post.haveAccess ? <div className="pp_post__text2">{post.content}</div> : null}
              </div>

              {post.haveAccess ? (
                <div className="pp_post__img" onClick={() =>setModalActive(true)}>
                  <img
                    className="pp_post__img"
                    src={post?.attachments?.[0]?.sourceUrl ?? ""}
                    alt=""
                  />
                                <Modal active ={modalActive} setActive={setModalActive}>
                <img
                  className=""
                  src={post?.attachments?.[0]?.sourceUrl ?? ""}
                />
              </Modal>
                </div>
              ) : (
                <div className="pp_post__img pp_blurred">
                  <img
                    className="pp_post__img"
                    src={post.attachments[0] ? post.attachments[0]!.sourceUrl : "/img/NoUserPhoto.svg"}
                    alt=""
                  />
                  <div className="pp_post__text_noaccess">
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
