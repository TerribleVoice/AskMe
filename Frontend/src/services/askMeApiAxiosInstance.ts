import axios from "axios";

export const askMeApiAxiosInstance = axios.create({
  baseURL: "http://localhost:7279",
  // baseURL: 'https://jsonplaceholder.typicode.com', // фейк апи
  withCredentials: true,
  headers: {
    // Authorization: process.env.API_TOKEN,
    // credentials: "include",
    // Accept: "application/json",
    Accept: 'accept: */*'
  },
});