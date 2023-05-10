import { IUserAuthentication } from "@/models/IUserAuthentication";
import { askMeApiAxiosInstance } from "./askMeApiAxiosInstance";

export const userAuthentication = async (userAuth: IUserAuthentication) => {
    const response = await askMeApiAxiosInstance.post(`/User/login`, userAuth);
//   const response = await askMeApiAxiosInstance.post(`/posts`, userAuth); // это запрос на фейк апи 
  const res = response.data;
  return res;
};
