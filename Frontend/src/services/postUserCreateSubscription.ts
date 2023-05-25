import { askMeApiAxiosInstance } from "./askMeApiAxiosInstance";
import { IUserCreateSubscription } from "@/models/IUserSubscriptions";

export const userCreateSubscription = async (userSubscription: IUserCreateSubscription) => {
  const response = await askMeApiAxiosInstance.post(`/Subscription/create`, {...userSubscription, parentSubscriptionId: `3fa85f64-5717-4562-b3fc-2c963f66afa6`});
  return response;
};