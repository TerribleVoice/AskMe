import { Link } from "react-router-dom";

export default function Author1(props) {
    return (
    <div>
    <Link to="/ObabMaster">
    <div className="Author">
            <div className="Authoravatar">
            <img src="img/profile/avatar2.jpg" height="180" width="180"/>
            </div>
            <div className="Authorname">
            ObabMaster
            </div>
            <div className="AuthorStatus">
                Один такой
            </div>
            <div className="Authorlink">
                Перейти в блог
            </div>
    </div>
    </Link>
    </div>
    )
};