import React, { FC } from "react";

interface ModalProps {
  active: boolean;
  setActive: (value: boolean) => void;
  children: React.ReactNode;
}

const Modal: FC<ModalProps> = ({ active, setActive }) => {
  return (
    <div className={active ? "modal active" : "modal"} onClick={() => setActive(false)}>
      <div className="modal_content">

      </div>
    </div>
  );
};

export default Modal;