import { IUserUpdatePostAttachments } from "@/models/IUserPosts";
import { askMeApiAxiosInstance } from "./askMeApiAxiosInstance";

export const userUpdatePostAttachments = async (
  userUpdatePostAttachments: IUserUpdatePostAttachments,
  id: string,
) => {
  const files = [userUpdatePostAttachments.files]
  console.log(files)
  const response = await askMeApiAxiosInstance.post(
    `/Feed/${id}/attachFiles`,
    { 
      files,
      postId: id 
    },
    { headers: { "Content-Type": "multipart/form-data" } }
  );
  return response;
};
