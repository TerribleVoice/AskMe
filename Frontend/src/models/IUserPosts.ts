export interface IUserPost {
  id: string;
  content: string;
  createAt: string;
  haveAccess: boolean;
  subscriptionName: string;
  authorViewModel: {
    login: string;
    description: string;
    links: string;
    profileImageUrl: string;
  };
}
export type IUserCreatePost = Required<
  Pick<IUserPost, "content" | "subscriptionName">
>;
