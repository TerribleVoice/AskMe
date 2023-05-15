import { IUserRegistration } from "@/models/IUserRegistration";
import { askMeApiAxiosInstance } from "./askMeApiAxiosInstance";

export const userRegistration = async (userReg: IUserRegistration) => {
  // const { status } = await askMeApiAxiosInstance.post(
  //   `/User/create`,
  //   userReg
  // );
  // return status;
    
  const response = await askMeApiAxiosInstance.post(`/posts`, userReg); // это запрос на фейк апи
  return response
};
