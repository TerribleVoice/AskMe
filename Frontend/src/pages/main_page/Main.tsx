import { Ask } from "@/pages/main_page/components/Ask/Ask";
import { Let } from "@/pages/main_page/components/Let/Let";
import { Service } from "@/pages/main_page/components/Service/Service";
import { Ourauthors } from "@/pages/main_page/components/Ourauthors/Ourauthors";

import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
import Slider from "react-slick";
import { IUserTopAuthors } from "@/models/IUserTopAuthors";
import { getUserTopAuthors } from "@/services/getTopAuthors";
import { useState, useEffect } from "react";
import { Author } from "./components/Ourauthors/Author";

export const Main = () => {
  const settings = {
    dots: false,
    infinite: false,
    speed: 950,
    slidesToShow: 3,
    slidesToScroll: 3,
  };
  const [authorData, setAuthorData] = useState<IUserTopAuthors[]>([]);
  useEffect(() => {
    try {
      const fetchData = async () => {
        const data = await getUserTopAuthors(5);
        if (data === undefined) {
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
  });
  return (
    <>
      <Ask />
      <Service />
      <Let />
      <Ourauthors />
      <div className="container">
        <Slider {...settings}>
          {authorData.map((author) => {
            return <Author login={author.login} description={author.description} links={author.links}/>
          })}
        </Slider>
      </div>
    </>
  );
};
