import axios from "axios";

export const askMeApiAxiosInstance = axios.create({
  baseURL: process.env.ASK_ME_API_URL,
  withCredentials: true,
  headers: {
    Authorization: process.env.API_TOKEN,
    "Notion-Version": "2022-06-28",
    Accept: "application/json",
  },
});
