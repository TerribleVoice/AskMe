import { IUserUpdatePost } from "@/models/IUserPosts";
import { askMeApiAxiosInstance } from "./askMeApiAxiosInstance";

export const postUserUpdatePost = async (
  userSubscriptionData: IUserUpdatePost,
  id: string
) => {
  const response = await askMeApiAxiosInstance.post(
    `/Feed/${id}/update`,
    userSubscriptionData,
    { headers: { "Content-Type": "multipart/form-data" } }
  );
  return response;
};
