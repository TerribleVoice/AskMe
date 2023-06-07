interface ModalProps {
  imageUrl: string;
  onClose: () => void;
}

export const Modal = ({ imageUrl, onClose }:ModalProps) => {
  return (
    <div className="modal">
      <div className="modal-content">
        <img src={imageUrl} alt="Modal" />
        <button className="close-button" onClick={onClose}>
          Close
        </button>
      </div>
    </div>
  );
};
