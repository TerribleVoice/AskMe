import { askMeApiAxiosInstance } from "./askMeApiAxiosInstance";
import { IUserPost } from "@/models/IUserPosts";

export const getUserFeed = async (userLogin: string) => {
  const { data } = await askMeApiAxiosInstance.get<IUserPost[]>(`/Feed/${userLogin}/feed`);
  return data;
};