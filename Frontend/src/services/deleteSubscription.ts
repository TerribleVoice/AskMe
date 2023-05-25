import { askMeApiAxiosInstance } from "./askMeApiAxiosInstance";

export const deleteSubscription = async (id: string) => {
  const response = await askMeApiAxiosInstance.delete(`/User/top_authors`, {
    params: { id },
  });
  return response;
};
