import { IUserPost } from "@/models/IUserPosts";
import { getUserPosts } from "@/services/getUserPosts";
import { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";

const zaglushka: IUserPost[] = [
  {
    id: "asdasdasd",
    content: "asdasdasd",
    createAt: "asdasdasd",
    haveAccess: true,
    subscriptionName: "asdasdasd",
    authorViewModel: {
      login: "asdasdasd",
      description: "asdasdasd",
      links: "asdasdasd",
      profileImageUrl: "asdasdasd",
    },
  },
];

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
            setPosts(zaglushka);
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
    } finally {
      setPosts(zaglushka);
    }
  }, [LoginName]);

  return (
    <>
      {posts && (
          posts.map((post) => (
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
                  <div className="pp_post__text2">{post.content}</div>
                </div>
              ) : (
                <div className="pp_post__img pp_blurred">
                  <img src="img/profile/photo.jpg" alt="profile"></img>
                  <div className="pp_post__text2">
                    <p>Пост только для платных подписчиков</p>
                    <p>{post.subscriptionName}</p>
                  </div>
                </div>
              )}
            </div>
          ))
      )}
    </>
  );
};
