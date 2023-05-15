import { IUserAuthentication } from "@/models/IUserAuthentication";
import { askMeApiAxiosInstance } from "./askMeApiAxiosInstance";

export const userAuthentication = async (userAuth: IUserAuthentication) => {
  // const { data } = await askMeApiAxiosInstance.post(`/User/login`, userAuth);
  // return data;
  const response = await askMeApiAxiosInstance.post(`/posts`, userAuth); // это запрос на фейк апи
  return response
};
