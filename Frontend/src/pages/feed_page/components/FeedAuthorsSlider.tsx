import { IUserTopAuthors } from "@/models/IUserTopAuthors";
import { getUserTopAuthors } from "@/services/getTopAuthors";
import { useEffect, useState } from "react";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
import Slider from "react-slick";
import { Link } from "react-router-dom";

export const FeedAuthorsSlider = () => {
  const settings = {
    dots: false,
    infinite: false,
    speed: 950,
    slidesToShow: 4,
    slidesToScroll: 3,
    innerWidth: "auto",
  };
  const [authorsData, setAuthorData] = useState<IUserTopAuthors[]>([]);
  useEffect(() => {
    try {
      const fetchData = async () => {
        const data = await getUserTopAuthors(7);
        if (data === undefined) {
          console.log(data);
          setAuthorData([]);
        } else {
          console.log(data);
          setAuthorData(data);
        }
      };
      fetchData();
    } catch (error) {
      console.log(error);
    }
  }, []);
  return (
    <div className={`feed_container`}>
      <Slider {...settings}>
        {authorsData.map((author) => {
          return (
            <div key={author.login} className="feed_author hover_create_subscr" > 
              <div className="feed_authoravatar">
                {author.profileImageUrl !== null ? (
                  <img className="feed_avatar" src={`${author.profileImageUrl}`} />
                ) : (
                  <img
                    className="feed_avatar"
                    src={`img/NoUserPhoto.svg`}
                    alt="noava"
                  />
                )}
              </div>
              <div className="feed_authorname">{author.login}</div>
              <div className="feed_authorlink">
                <Link to={`/${author.login}`}>Перейти в блог</Link>
              </div>
            </div>
          );
        })}
      </Slider>
    </div>
  );
};
