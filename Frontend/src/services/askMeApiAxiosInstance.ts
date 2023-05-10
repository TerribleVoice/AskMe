import axios from "axios";

export const askMeApiAxiosInstance = axios.create({
  baseURL: process.env.ASK_ME_API_URL,
  // baseURL: 'https://jsonplaceholder.typicode.com', // фейк апи
  withCredentials: true,
  headers: {
    Authorization: process.env.API_TOKEN,
    credentials: "include",
    Accept: "application/json",
  },
});
