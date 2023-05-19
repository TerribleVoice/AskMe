import { Link } from "react-router-dom";

export const Author4 = () => {
  return (
    <div className="Author">
      <div className="Authoravatar">
        <img src="img/profile/avatar4.jpg" height="180" width="180" alt="avatar4.jpg" />
      </div>
      <div className="Authorname">NeDlaProdagi</div>
      <div className="Authorlink">
        <Link to="/NeDlaProdagi">Перейти в блог</Link>
      </div>
    </div>
  );
};
