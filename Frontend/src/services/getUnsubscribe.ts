import { askMeApiAxiosInstance } from "./askMeApiAxiosInstance";

export const getUnsubscribe = async (id: string) => {
  const response = await askMeApiAxiosInstance.get(`/Subscription/${id}/unsubscribe`);
  return response;
};
