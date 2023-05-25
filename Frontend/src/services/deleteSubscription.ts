import { askMeApiAxiosInstance } from "./askMeApiAxiosInstance";

export const deleteSubscription = async (id: string) => {
  const response = await askMeApiAxiosInstance.delete(`/Subscription/delete`, {
    params: { id },
  });
  return response;
};
