import { useState } from "react";
import ReactAudioPlayer from "react-audio-player";
import { FaPlay, FaPause } from "react-icons/fa";

interface IAttachment {
  fileType: number;
  sourceUrl: string;
}
export const Attachment = ({ fileType, sourceUrl }: IAttachment) => {
  switch (fileType) {
    case 0:
      return (
        <img
          className="pp_post__img pp_post__img_attach"
          src={sourceUrl}
          alt="."
        />
      );
    case 1:
      return (
        <video className="pp_post__video_attach" controls>
          <source src={sourceUrl} type="video/mp4" />
          Your browser does not support the video element.
        </video>
      );
    case 2:
      return <div className="pp_post__text_attach">{sourceUrl}</div>;
    default:
      return <></>;
  }
};
