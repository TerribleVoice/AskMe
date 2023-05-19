import { IUserAuthentication } from "@/models/IUserAuthentication";
import { askMeApiAxiosInstance } from "./askMeApiAxiosInstance";

export const userAuthentication = async (userAuth: IUserAuthentication) => {
  const response = await askMeApiAxiosInstance.post(`/User/login`, userAuth);
  return response;
};
