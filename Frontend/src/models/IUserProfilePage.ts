export interface IUserProfilePage {
  login: string;
  isAuthor: boolean;
  description?: string;
  status?: string;
  links?: string[];
  posts?: IUserPost[];
}
export interface IUserPost {
  id: string;
  content?: string;
  price?: number;
  createAt: string;
  haveAccess: boolean;
  subscriptionName?: string;
}
export type IUserCreatePost = Required<Pick<
  IUserPost,
  "content" | "price" | "subscriptionName"
>>;
