//import "./main_page.css";

import { Ask } from "@/pages/main_page/components/Ask/Ask";
import { Let } from "@/pages/main_page/components/Main/Let/Let";
import { Service } from "@/pages/main_page/components/Service/Service";
import { Author1 } from "@/pages/main_page/components/Main/Ourauthors/Author1";
import { Author2 } from "@/pages/main_page/components/Main/Ourauthors/Author2";
import { Author3 } from "@/pages/main_page/components/Main/Ourauthors/Author3";
import { Author4 } from "@/pages/main_page/components/Main/Ourauthors/Author4";
import { Ourauthors } from "@/pages/main_page/components/Main/Ourauthors/Ourauthors";

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
    <>
      <Ask />
      <Service />
      <Let />
      <Ourauthors />
      <div className="container">
        <Slider {...settings}>
          {/* Здесь нужен эндпоинт на получение авторов */}
          <Author1 />
          <Author2 />
          <Author3 />
          <Author4 />
        </Slider>
      </div>
    </>
  );
};
