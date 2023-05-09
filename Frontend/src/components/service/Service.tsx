export const Service = () => {
  return (
    <div className="service">
      <div className="service__img">
        <img src="img/person.png" alt="person.png" />
      </div>
      <div className="service__right">
        <div className="service__title">
          <span>AskMe</span> - это удобный сервис по сбору денег для:
        </div>
        <div className="service__points">
          <ul>
            <li>художников</li>
            <li>музыкантов</li>
            <li>стримеров</li>
            <li>различных проектов</li>
          </ul>
        </div>
      </div>
    </div>
  );
};
