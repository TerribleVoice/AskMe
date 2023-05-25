import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
import Slider from "react-slick";

import { AuthorsSliderProp } from "@/models/IUserTopAuthors";
import { Author } from "./Author";

export const AuthorsSlider = ({authorsData}: AuthorsSliderProp) => {
  const settings = {
    dots: false,
    infinite: false,
    speed: 950,
    slidesToShow: 3,
    slidesToScroll: 3,
  };
  return (
    <div className={`container`}>
      <Slider {...settings}>
        {authorsData.map((author) => {
        return <Author key={author.login} author={author} />
      })}
      </Slider>
    </div>
  );
};
