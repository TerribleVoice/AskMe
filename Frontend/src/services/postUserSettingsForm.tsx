import { IUserSettings } from "@/models/IUserSettings";
import { askMeApiAxiosInstance } from "./askMeApiAxiosInstance";

export const postUserSettingsForm = async (
  data: IUserSettings
) => {
  const response = await askMeApiAxiosInstance.post(
    `/User/update`,
    data
  );
  return response;
};
