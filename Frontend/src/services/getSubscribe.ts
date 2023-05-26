import { askMeApiAxiosInstance } from "./askMeApiAxiosInstance";

export const getSubscribe = async (id: string) => {
  const response = await askMeApiAxiosInstance.get(`/Subscription/${id}/subscribe`);
  return response;
};