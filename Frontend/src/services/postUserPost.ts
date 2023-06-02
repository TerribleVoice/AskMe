import { IUserCreatePost } from "@/models/IUserPosts";
import { askMeApiAxiosInstance } from "./askMeApiAxiosInstance";

export const userCreatePost = async (userPost: any) => {
  try {
    const response = await askMeApiAxiosInstance.post(
      "/Feed/create",
      userPost,
      { headers: { "Content-Type": "multipart/form-data" } }
    );
    return response;
  } catch (error) {
    throw error;
  }
};
