import { askMeApiAxiosInstance } from "./askMeApiAxiosInstance";
import { IUserEditSubscription } from "@/models/IUserSubscriptions";

export const userEditSubscription = async (
  userSubscriptionData: IUserEditSubscription,
  id: string,
) => {
  const response = await askMeApiAxiosInstance.post(
    `/Subscription/${id}/update`,
    userSubscriptionData
  );
  return response;
};
