import { IUserPhoto } from "@/models/IUserSettings";
import { askMeApiAxiosInstance } from "./askMeApiAxiosInstance";

export const postUserPhoto = async (photo: IUserPhoto, userLogin: string) => {
  console.log(photo);
  const formData = new FormData();
  formData.append("image", photo.image![0]);
  const response = await askMeApiAxiosInstance.post(
    `/User/${userLogin}/profile_image`,
    photo,
    { headers: { "Content-Type": "multipart/form-data" } }
  );
  return response;
};
