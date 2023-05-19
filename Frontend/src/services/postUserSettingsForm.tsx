import { IUserSettings } from "@/models/IUserSettings";
import { askMeApiAxiosInstance } from "./askMeApiAxiosInstance";

export const postUserSettingsForm = async (
  userLogin: string,
  data: IUserSettings
) => {
  const response = await askMeApiAxiosInstance.post(
    `/Subscription/${userLogin}/created_list`,
    data
  );
  return response;
};
