import { IUserUpdatePostAttachments } from "@/models/IUserPosts";
import { IUserPhoto } from "@/models/IUserSettings";
import { userUpdatePostAttachments } from "@/services/postUserUpdatePostAttachments";
import { ChangeEvent, useState } from "react";
import { Controller, useForm, SubmitHandler } from "react-hook-form";
import { useNavigate, useParams } from "react-router-dom";

interface IEditAttachPost {
  postId: string;
}

export const EditAttachPost = ({ postId }: IEditAttachPost) => {
  const {
    handleSubmit,
    formState: { errors },
    control,
  } = useForm<IUserUpdatePostAttachments>();

  const { LoginName } = useParams();
  const [selectedImage, setSelectedImage] = useState<string | null>(null);
  const navigation = useNavigate();

  const handleFileChange = (event: ChangeEvent<HTMLInputElement>) => {
    console.log(event.target);
    const file = event.target.files?.[0];
    console.log(file);
    if (file) {
      setSelectedImage(URL.createObjectURL(file));
    }
    return file;
  };

  const onAttachmentsSubmit: SubmitHandler<IUserUpdatePostAttachments> = async (
    data
  ) => {
    try {
      if (!data) {
        console.log(data);
      }
      console.log(data);
      const response = await userUpdatePostAttachments(data, postId);
      console.log(response);
      if (response.status < 300) {
        navigation(`/${LoginName}`);
      } else {
        alert("Reject");
      }
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <form
      className="settings_form"
      onSubmit={handleSubmit(onAttachmentsSubmit)}
    >
      <div className="subscription_image">
        <label htmlFor="image">Обложка поста</label>
        {selectedImage && (
          <div>
            <img id="image-preview" src={selectedImage} alt="Uploaded" />
          </div>
        )}
        <label className="custom_file_upload">
          <Controller
            control={control}
            name="files"
            render={({ field }) => (
              <input
                {...field}
                onChange={(event) => field.onChange(handleFileChange(event))}
                type="file"
                id="files"
                value={undefined}
              />
            )}
          />
          ВЫБРАТЬ ФАЙЛ
        </label>
      </div>
      <p className="left-reg__submit">
        <button type="submit">Сохранить</button>
      </p>
    </form>
  );
};
