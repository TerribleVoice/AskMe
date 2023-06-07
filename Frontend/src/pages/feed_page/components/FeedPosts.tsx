import { IUserPost } from "@/models/IUserPosts";
import { getUserFeed } from "@/services/getUserFeed";
import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { zaglushkaPosts } from "./zaglushkaPosts";

export const FeedPosts = () => {
  const LoginName = localStorage.getItem("login");
  const navigate = useNavigate();
  const [posts, setPosts] = useState<IUserPost[]>([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        if (LoginName !== undefined) {
          const data = await getUserFeed(LoginName!);
          // setPosts(zaglushkaPosts); // заглушка
          setPosts(data);
          console.log(data);
        } else {
          console.log(LoginName);
          navigate("/404");
        }
      } catch (error) {
        console.log(error);
        setPosts(zaglushkaPosts);
      }
    };
    fetchData();
  }, [LoginName, navigate]);

  return (
    <div className="pp_posts_wrapper"> {/*feed_posts_wrapper*/}
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
              </div>
              <div
                className="pp_post__text"
                style={{ backgroundColor: "#181818" }}
              >
                <div className="pp_post__title">{post.title}</div>
                {post.haveAccess ? <div className="pp_post__text2">{post.content}</div> : null}
              </div>
              {post.haveAccess ? (
                <div className="pp_post__img">
                  <img
                    className="pp_post__img"
                    src={post?.attachments?.[0]?.sourceUrl ?? ""}
                    alt=""
                  />
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
