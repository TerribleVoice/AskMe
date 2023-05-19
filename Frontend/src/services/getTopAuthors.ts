import { IUserTopAuthors } from "@/models/IUserTopAuthors";
import { askMeApiAxiosInstance } from "./askMeApiAxiosInstance";

export const getUserTopAuthors = async (limit: number) => {
  const { data } = await askMeApiAxiosInstance.get<IUserTopAuthors[]>(`/User/top_authors`, { params: {limit: limit}});
  return data;
};
