export default function Service(props) {
    return (
        <div className="service">
          <div className="service__img">
            <img src="img/person.png" alt />
          </div>
          <div className="service__right">
            <div className="service__title">
              <span>AskMe</span> - это удобный сервис по сбору денег для:
            </div>
            <div className="service__points">
              <ul>
                <li>художников;</li>
                <li>музыкантов;</li>
                <li>стримеров;</li>
                <li>различных проектов;</li>
                <li>и много другого...</li>
              </ul>
            </div>
          </div>
        </div>
    );
};
