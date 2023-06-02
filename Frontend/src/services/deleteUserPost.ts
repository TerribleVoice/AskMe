import { askMeApiAxiosInstance } from "./askMeApiAxiosInstance";

export const deleteUserPost = async (postId: string) => {
  const response = await askMeApiAxiosInstance.delete(`/Feed/${postId}`);
  return response;
};