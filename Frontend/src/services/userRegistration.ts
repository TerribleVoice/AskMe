import { askMeApiAxiosInstance } from "./askMeApiAxiosInstance";

export const userRegistration = async () => {
  const response = await askMeApiAxiosInstance.post(`/User/login`, {});
  const res = response.data;
  return res;
};