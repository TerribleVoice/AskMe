import { askMeApiAxiosInstance } from "./askMeApiAxiosInstance";

export const deleteUserPhoto = async (userLogin: string) => {
  const response = await askMeApiAxiosInstance.delete(`/User/${userLogin}/profile_image`);
  return response;
};