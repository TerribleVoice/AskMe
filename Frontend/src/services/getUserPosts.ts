import { askMeApiAxiosInstance } from "./askMeApiAxiosInstance";
import { IUserPost } from "@/models/IUserPosts";

export const getUserPosts = async (userLogin: string) => {
  const { data } = await askMeApiAxiosInstance.get<IUserPost[]>(`/Feed/${userLogin}/posts`);
  return data;
};