import { askMeApiAxiosInstance } from "./askMeApiAxiosInstance";

export const userCreatePost = async (userPost: FormData) => {
  try {
    const response = await askMeApiAxiosInstance.post("/Feed/create", userPost, {
      headers: { "Content-Type": "multipart/form-data" },
    });
    return response;
  } catch (error) {
    throw error;
  }
};
