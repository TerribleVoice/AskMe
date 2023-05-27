import { IUserPost } from "@/models/IUserPosts";
import { zaglushkaPosts } from "@/pages/feed_page/components/zaglushkaPosts";
import { getUserPosts } from "@/services/getUserPosts";
import { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";

export const Posts = () => {
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
              <div className="pp_post__date" style={{ marginLeft: "330px" }}>
                {post.createAt}
              </div>
            </div>
            <div className="pp_post__title" style={{backgroundColor: "#181818"}}>
              <div className="pp_post__text">{post.title}</div>
            </div>
            {post.haveAccess ? (
              <div className="pp_post__img">
                <img
                  className="pp_post__img"
                  src="img/profile/photo.jpg"
                  alt="."
                />
                <div className="pp_post__text2">{post.content}</div>
              </div>
            ) : (
              <div className="pp_post__img pp_blurred">
                <img
                  className="pp_post__img"
                  src="img/profile/photo.jpg"
                  alt="."
                />
                <div className="pp_post__text2">
                  <p>Пост только для платных подписчиков</p>
                </div>
              </div>
            )}
          </div>
        ))}
    </div>
  );
};
