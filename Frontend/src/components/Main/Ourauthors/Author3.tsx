import { Link } from "react-router-dom";

export const Author3 = () => {
  return (
    <div className="Author">
      <div className="Authoravatar">
        <img src="img/profile/avatar3.jpg" height="180" width="180" alt="avatar3.jpg" />
      </div>
      <div className="Authorname">YOUNG77</div>
      <div className="Authorlink">
        <Link to="/YOUNG77">Перейти в блог</Link>
      </div>
    </div>
  );
};
