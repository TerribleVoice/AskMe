import { Link } from "react-router-dom";

export const Author2 = () => {
  return (
    <div className="Author">
      <div className="Authoravatar">
        <img src="img/profile/avatar2.jpg" height="180" width="180" alt="avatar2.jpg" />
      </div>
      <div className="Authorname">ObabMaster</div>
      <div className="Authorlink">
        <Link to="/ObabMaster">Перейти в блог</Link>
      </div>
    </div>
  );
};
