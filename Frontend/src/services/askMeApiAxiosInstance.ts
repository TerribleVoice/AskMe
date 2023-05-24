import axios from "axios";

export const askMeApiAxiosInstance = axios.create({
  baseURL: process.env.REACT_APP_ASK_ME_API_URL, 
  withCredentials: true,
  headers: {
    Accept: 'accept: */*'
  },
});