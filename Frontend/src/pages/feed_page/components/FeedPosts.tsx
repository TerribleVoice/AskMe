import { IUserPost } from "@/models/IUserPosts";
import { getUserFeed } from "@/services/getUserFeed";
import { useState, useEffect } from "react";
import { useParams, useNavigate } from "react-router-dom";

const zaglushka: IUserPost[] = [
  {
    id: "asdasdasd",
    content: "asdasdasd",
    createAt: "asdasdasd",
    haveAccess: true,
    title: "asdasdasd",
    authorViewModel: {
      login: "asdasdasd",
      description: "asdasdasd",
      links: "asdasdasd",
      profileImageUrl: "asdasdasd",
    },
  },
];

export const FeedPosts = () => {
  const LoginName = localStorage.getItem("login");
  const navigate = useNavigate();
  const [posts, setPosts] = useState<IUserPost[]>([]);
  
  useEffect(() => {
    const fetchData = async () => {
      try {
        if (LoginName !== undefined) {
          const data = await getUserFeed(LoginName!);
          setPosts(data ?? zaglushka);
        } else {
            console.log(LoginName)
          navigate("/404");
        }
      } catch (error) {
        console.log(error);
        setPosts(zaglushka);
      }
    };
    fetchData();
  }, [LoginName]);

  return (
    <>
      {posts.map((post) => (
        <div key={post.id} className="pp_post">
          <div className="pp_post__title">
            <div className="pp_post__text">{post.title}</div>
            <div className="pp_post__date">{post.createAt}</div>
          </div>
          {post.haveAccess ? (
            <div className="pp_post__img">
              <div className="pp_post__text2">{post.content}</div>
            </div>
          ) : (
            <div className="pp_post__img pp_blurred">
              <img src="img/profile/photo.jpg" alt="profile" />
              <div className="pp_post__text2">
                <p>Пост только для платных подписчиков</p>
              </div>
            </div>
          )}
        </div>
      ))}
    </>
  );
};
