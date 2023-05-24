import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
import Slider from "react-slick";
import { Author1 } from "./Author1";
import { Author2 } from "./Author2";
import { Author3 } from "./Author3";
import { Author4 } from "./Author4";

interface AuthorsSliderProp {
  className: string
}

export const AuthorsSlider = ({className}: AuthorsSliderProp) => {
  const settings = {
    dots: false,
    infinite: false,
    speed: 950,
    slidesToShow: 3,
    slidesToScroll: 3,
  };
  return (
    <div className={`${className}`}>
      <Slider {...settings}>
        {/* {authorData.map((author) => {
        return <Author login={author.login} description={author.description} links={author.links}/>
      })} */}
        <Author1 />
        <Author2 />
        <Author3 />
        <Author4 />
      </Slider>
    </div>
  );
};
