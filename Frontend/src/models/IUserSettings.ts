export interface IUserSettings {
  login: string | null;
  email: string | null;
  oldLogin: string | null;
  links: string | null;
  description: string | null;
  password: string | null;
}
export interface IUserPhoto {
  image?: FileList;
}
