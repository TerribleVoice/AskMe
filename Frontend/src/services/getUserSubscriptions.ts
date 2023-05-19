import { IUserSubscriptions } from "@/models/IUserSubscriptions";
import { askMeApiAxiosInstance } from "./askMeApiAxiosInstance";

export const getUserSubscriptions = async (userLogin: IUserSubscriptions) => {
  const { data } = await askMeApiAxiosInstance.get<IUserSubscriptions>(
    `/Subscription/${userLogin}/created_list`
  );
  return data;
};
