import { IUserPost } from "@/models/IUserPosts";

export const zaglushkaPosts: IUserPost[] = [
  {
    id: "1235456687",
    content:
      "Content1 Content1 Content1 Content1 Content1 Content1 Content1 Content1 Content1 ",
    createAt: "2021.07.25 19:54",
    haveAccess: true,
    title: "title1",
    authorViewModel: {
      login: "user1",
      description: "description1",
      links: "https://link1.com",
      profileImageUrl: "/img/NoUserPhoto.svg",
    },
    attachments: [
      {
        fileType: 0,
        sourceUrl: "string",
      },
    ],
  },
  {
    id: "12354566872",
    content: "asdasdasd",
    createAt: "2021.07.25 09:54",
    haveAccess: true,
    title: "title2",
    authorViewModel: {
      login: "user2",
      description: "description2",
      links: "asdasdasd",
      profileImageUrl: "/img/NoUserPhoto.svg",
    },
    attachments: [
      {
        fileType: 0,
        sourceUrl: "string",
      },
    ],
  },
  {
    id: "12354566873",
    content: "asdasdasd",
    createAt: "2021.07.22 21:47",
    haveAccess: true,
    title: "title3",
    authorViewModel: {
      login: "user3",
      description: "description3",
      links: "asdasdasd",
      profileImageUrl: "/img/NoUserPhoto.svg",
    },
    attachments: [
      {
        fileType: 0,
        sourceUrl: "string",
      },
    ],
  },
  {
    id: "12354566875",
    content: "asdasdasd",
    createAt: "2021.07.22 11:23",
    haveAccess: true,
    title: "title3",
    authorViewModel: {
      login: "user4",
      description: "description4",
      links: "asdasdasd",
      profileImageUrl: "/img/NoUserPhoto.svg",
    },
    attachments: [
      {
        fileType: 0,
        sourceUrl: "string",
      },
    ],
  },
];
