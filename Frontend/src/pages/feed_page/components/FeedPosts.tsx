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
    <div className="feed_posts_wrapper">
      {posts &&
        posts.map((post) => (
          <div key={post.id} className="pp_post">
            <div
              style={{
                display: "flex",
                flexDirection: "row",
                alignItems: "center",
                backgroundColor: "#181818",
              }}
            >
              {!post.authorViewModel.profileImageUrl ? (
                <img
                  src={`${post.authorViewModel.profileImageUrl}`}
                  style={{ width: "50px", margin: "20px" }}
                  alt="."
                />
              ) : (
                <img
                  src={`/img/NoUserPhoto.svg`}
                  style={{ width: "50px", margin: "20px" }}
                  alt="."
                />
              )}
              <span style={{ fontSize: "20px" }}>
                {post.authorViewModel.login}
              </span>
              <div className="pp_post__date" style={{ marginLeft: "25vw", marginRight: "20px"}}>
                {post.createAt}
              </div>
            </div>
            <div
              className="pp_post__title"
              style={{ backgroundColor: "#181818" }}
            >
              <div className="pp_post__text">{post.title}</div>
            </div>
            {/* {post.haveAccess ? (
              <div className="pp_post__img">
                <img
                  className="pp_post__img"
                  src="img/profile/photo.jpg"
                  alt="profile"
                />
                <div className="pp_post__text2">{post.content}</div>
              </div>
            ) : (
              <div className="pp_post__img pp_blurred">
                <img
                  className="pp_post__img"
                  src="img/profile/photo.jpg"
                  alt="profile"
                ></img>
                <div className="pp_post__text2">
                  <p>Пост только для платных подписчиков</p>
                </div>
              </div>
            )} */}
          </div>
        ))}
    </div>
  );
};
