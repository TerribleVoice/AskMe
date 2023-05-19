import { askMeApiAxiosInstance } from "./askMeApiAxiosInstance";
import { IUserCreateSubscription } from "@/models/IUserSubscriptions";

export const userCreateSubscription = async (userSubscription: IUserCreateSubscription) => {
  const response = await askMeApiAxiosInstance.post(`/create`, userSubscription);
  return response;
};