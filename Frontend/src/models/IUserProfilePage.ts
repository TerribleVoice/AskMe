export interface IUserProfilePage {
  login: string;
  isAuthor: boolean;
  description?: string;
  status?: string;
  links?: string[];
  posts?: PostViewModel[];
}
export interface PostViewModel {
  id: string;
  content?: string;
  price?: number;
  createAt: string;
  haveAccess: boolean;
  subscriptionName?: string;
}
