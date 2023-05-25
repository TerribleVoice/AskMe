import { AuthorProp } from "@/models/IUserTopAuthors";
import { Link } from "react-router-dom";

export const Author = ({author}: AuthorProp) => {
  return (
    <div className="Author">
      <div className="Authoravatar">
        <img
          src={`${author.profileImageUrl}`}
        />
      </div>
      <div className="Authorname">{author.login}</div>
      <div className="Authorlink">
        <Link to={`/${author.login}`}>Перейти в блог</Link>
      </div>
    </div>
  );
};
