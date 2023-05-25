export interface IUserTopAuthors {
  login: string;
  description: string;
  links: string;
  profileImageUrl: string;
}
export interface AuthorsSliderProp {
  authorsData: IUserTopAuthors[];
}
export interface AuthorProp {
  author: IUserTopAuthors;
}
