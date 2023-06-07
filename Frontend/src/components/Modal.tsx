import React, { FC } from "react";

interface ModalProps {
  active: boolean;
  setActive: (value: boolean) => void;
}

const Modal: FC<ModalProps> = ({ active, setActive }) => {
  return (
    <div className="modal">
      <div className="modal_content"></div>
    </div>
  );
};

export default Modal;