import { askMeApiAxiosInstance } from "./askMeApiAxiosInstance";
import { IUserCreatePost } from "@/models/IUserProfilePage";

export const userCreatePost = async (userPost: IUserCreatePost) => {
  const response = await askMeApiAxiosInstance.post(`/Feed/create`, userPost);
  return response;
};