import React from "react";
import { useNavigate } from "react-router-dom";

export const GoBack: React.FC = () => {
  const navigate = useNavigate();
  const onGoBack = () => navigate(-1);
  return (
    <div className="go_back" onClick={onGoBack}>
      <img className="back_image" src="/img/Arrow_2405.svg" alt="Назад" />
      <span className="back">Назад</span>
    </div>
  );
};
