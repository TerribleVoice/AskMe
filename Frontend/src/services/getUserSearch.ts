import { IUserSearch } from "@/models/IUserSearch";
import { askMeApiAxiosInstance } from "./askMeApiAxiosInstance";

export const getUserSearch = async (query: string) => {
  const { data } = await askMeApiAxiosInstance.get<IUserSearch[]>(
    `/User/search?`,
    { params: { query: query, limit: 5 } }
  );
  return data;
};
