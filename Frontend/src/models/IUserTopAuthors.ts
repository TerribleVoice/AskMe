export interface IUserTopAuthors {
  login: string;
  description: string;
  links: string;
  profileImageUrl: string | null;
}
export interface AuthorsSliderProp {
  authorsData: IUserTopAuthors[];
}
export interface AuthorProp {
  author: IUserTopAuthors;
}
