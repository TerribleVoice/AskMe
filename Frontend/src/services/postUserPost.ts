import { IUserCreatePost } from "@/models/IUserPosts";
import { askMeApiAxiosInstance } from "./askMeApiAxiosInstance";

export const userCreatePost = async (userPost: any) => {
  try {
    const response = await askMeApiAxiosInstance.post("/Feed/create", userPost);
    return response;
  } catch (error) {
    throw error;
  }
};
