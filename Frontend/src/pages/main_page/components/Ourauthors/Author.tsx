import { IUserTopAuthors } from "@/models/IUserTopAuthors";
import { Link } from "react-router-dom";

export const Author = ({login, description, links}: IUserTopAuthors) => {
  return (
    <div className="Author">
      <div className="Authoravatar">
        <img
          src="img/profile/avatar1.jpg"
          height="180"
          width="180"
          alt="avatar1.jpg"
        />
      </div>
      <div className="Authorname">{login}</div>
      <div className="Authorlink">
        <Link to={`/${login}`}>Перейти в блог</Link>
      </div>
      <div>{description}</div>
      <div>{links}</div>
    </div>
  );
};
