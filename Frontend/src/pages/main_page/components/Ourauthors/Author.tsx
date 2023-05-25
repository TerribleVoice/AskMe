import { AuthorProp } from "@/models/IUserTopAuthors";
import { Link } from "react-router-dom";

export const Author = ({ author }: AuthorProp) => {
  const image = author.profileImageUrl;
  return (
    <div key={author.login} className="Author">
      <div className="Authoravatar">
        {image !== null ? (
          <img className="pp_left__avatar" src={`${image}`} />
        ) : (
          <img
            className="pp_left__avatar"
            src={`img/NoUserPhoto.svg`}
            alt="noava"
          />
        )}
      </div>
      <div className="Authorname">{author.login}</div>
      <div className="Authorlink">
        <Link to={`/${author.login}`}>Перейти в блог</Link>
      </div>
    </div>
  );
};
