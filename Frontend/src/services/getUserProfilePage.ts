import { IUserProfilePage } from "@/models/IUserProfilePage";
import { askMeApiAxiosInstance } from "./askMeApiAxiosInstance";

export const getUserProfilePage = async (userLogin: string) => {
  const { data } = await askMeApiAxiosInstance.get<IUserProfilePage>(`/User/${userLogin}`);
  return data;
};
