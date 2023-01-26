import { Link } from "react-router-dom";

export default function Author1(props) {
    return (

    <div className="Author">
            <div className="Authoravatar">
            <img src="profile/img/avatar3.jpg" height="180" width="180"/>
            </div>
            <div className="Authorname">
            Автор 3
            </div>
            <div className="Authorlink" >
            <a href="profile.html"></a>
            <Link to="/auth">
                Перейти в блог
            </Link>
            </div>
    </div>
    )
};