import axios from "axios";

export const askMeApiAxiosInstance = axios.create({
  baseURL: "http://localhost:7279",
  withCredentials: true,
  headers: {
    Accept: 'accept: */*'
  },
});