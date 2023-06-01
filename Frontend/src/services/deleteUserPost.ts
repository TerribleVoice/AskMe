import { askMeApiAxiosInstance } from "./askMeApiAxiosInstance";

export const deleteUserPhoto = async (postId: string) => {
  const response = await askMeApiAxiosInstance.delete(`/Feed/${postId}`);
  return response;
};