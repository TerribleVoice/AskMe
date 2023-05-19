import { IUserSubscriptions } from "@/models/IUserSubscriptions";
import { askMeApiAxiosInstance } from "./askMeApiAxiosInstance";

export const getUserBoughtSubscriptions = async (userLogin: string) => {
  const { data } = await askMeApiAxiosInstance.get<IUserSubscriptions[]>(`/Subscription/${userLogin}/bought_list`);
  return data;
};
