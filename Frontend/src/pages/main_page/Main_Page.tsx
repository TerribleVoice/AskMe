import { Ask } from "@/pages/main_page/components/Ask/Ask";
import { Let } from "@/pages/main_page/components/Let/Let";
import { Service } from "@/pages/main_page/components/Service/Service";
import { Ourauthors } from "@/pages/main_page/components/Ourauthors/Ourauthors";
import { AuthorsSlider } from "./components/Ourauthors/AuthorsSlider";

import { IUserTopAuthors } from "@/models/IUserTopAuthors";
import { getUserTopAuthors } from "@/services/getTopAuthors";
import { useState, useEffect } from "react";

export const Main = () => {
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
  }, []);
  return (
    <>
      <Ask />
      <Service />
      <Let />
      <Ourauthors />
      <AuthorsSlider authorsData={authorData} />
    </>
  );
};
