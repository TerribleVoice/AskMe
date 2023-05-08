//import "./main_page.css";

import { Ask } from "@/components/Ask/Ask";
import { Footer } from "@/components/main/footer/Footer";
import { Let } from "@/components/main/let/Let";
import { Service } from "@/components/service/Service";
import { Author1 } from "@/components/main/ourauthors/Author1";
import { Author2 } from "@/components/main/ourauthors/Author2";
import { Author3 } from "@/components/main/ourauthors/Author3";
import { Author4 } from "@/components/main/ourauthors/Author4";
import { Ourauthors } from "@/components/main/ourauthors/Ourauthors";

import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
import Slider from "react-slick";

export const Main = () => {
  const settings = {
    dots: false,
    infinite: false,
    speed: 950,
    slidesToShow: 3,
    slidesToScroll: 3,
  };
  return (
    <div>
      <div className="container">
        <Ask />
      </div>
      <Service />
      <div className="container">
        <Let />
      </div>
      <div className="container1">
        <Ourauthors />
      </div>
      <div className="container">
        <Slider {...settings}>
          <div className="container1">
            <Author1 />
          </div>
          <div className="container1">
            <Author2 />
          </div>
          <div className="container1">
            <Author3 />
          </div>
          <div className="container1">
            <Author4 />
          </div>
        </Slider>
      </div>
      <footer className="footer">
        <Footer />
      </footer>
    </div>
  );
};
