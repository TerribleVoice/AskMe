import { IUserCreatePost } from "@/models/IUserPosts";
import { askMeApiAxiosInstance } from "./askMeApiAxiosInstance";

export const userCreatePost = async (userPost: IUserCreatePost) => {
  const response = await askMeApiAxiosInstance.post(`/Feed/create`, userPost);
  return response;
};