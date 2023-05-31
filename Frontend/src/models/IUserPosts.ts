export interface IUserPost {
  id: string;
  content: string;
  createAt: string;
  haveAccess: boolean;
  title: string;
  authorViewModel: {
    login: string;
    description: string;
    links: string;
    profileImageUrl: string;
  };
}
export interface IUserCreatePost {
  Title: string;
  SubscriptionId: string;
  Content: string;
  attachments: FileList;
}
