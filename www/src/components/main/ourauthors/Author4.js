import { Link } from "react-router-dom";

export default function Author1(props) {
    return (

    <div className="Author">
            <div className="Authoravatar">
            <img src="img/profile/avatar4.jpg" height="180" width="180"/>
            </div>
            <div className="Authorname">
            Автор 4
            </div>
            <div className="Authorlink" >
            <Link to="/auth">
                Перейти в блог
            </Link>
            </div>
    </div>
    )
};