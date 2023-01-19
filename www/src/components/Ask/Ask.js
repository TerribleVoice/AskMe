import { Link } from "react-router-dom";

export default function Ask(props) {
    return (
        <div className="ask">
            <div className="left">
              <div className="left__title">
                <img src="img/AskMe.png" alt />
              </div>
              <div className="left__text">Amet minim mollit non deserunt ullamco est sit aliqua dolor do amet sint. </div>
              <Link to="/auth">
                <div className="left__btn">Приступить</div>
              </Link>
            </div>
            <div className="right">
              <img src="img/face.png" alt />
            </div>
          </div>
    )
};
