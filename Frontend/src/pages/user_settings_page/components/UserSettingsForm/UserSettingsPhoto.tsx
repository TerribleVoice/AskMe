import { IUserPhoto } from "@/models/IUserSettings";
import { postUserPhoto } from "@/services/postUserPhoto";
import { ChangeEvent, useState } from "react";
import { Controller, useForm, SubmitHandler } from "react-hook-form";
import { useParams } from "react-router-dom";

export const UserSettingsPhoto = () => {
  const {
    handleSubmit,
    formState: { errors },
    control,
  } = useForm<IUserPhoto>();

  const { LoginName } = useParams();
  const [selectedImage, setSelectedImage] = useState<string | null>(null);

  const handleFileChange = (event: ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    if (file) {
      setSelectedImage(URL.createObjectURL(file));
    }
    return file;
  };

  const onPhotoSubmit: SubmitHandler<IUserPhoto> = async (data) => {
    try {
      if (!data) {
        console.log(data)
      }
      const response = await postUserPhoto(data, LoginName!);

      if (response.status < 300) {
        alert("Confirm");
      } else {
        alert("Reject");
      }
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <form className="settings_form" onSubmit={handleSubmit(onPhotoSubmit)}>
      <div className="subscription_image">
        <label htmlFor="image">Аватар</label>
        {selectedImage && (
          <div>
            <img id="image-preview" src={selectedImage} alt="Uploaded" />
          </div>
        )}
        <label className="custom_file_upload">
          <Controller
            control={control}
            name="image"
            render={({ field }) => (
              <input
                {...field}
                onChange={(event) => field.onChange(handleFileChange(event))}
                type="file"
                id="image"
                value={undefined}
              />
            )}
          />
          ВЫБРАТЬ ФАЙЛ
        </label>
        <label className="settings_caption" htmlFor="description">
          Рекомендуемый размер 240х150 рх
        </label>
      </div>
      <p className="left-reg__submit">
        <button type="submit">Сохранить Фото</button>
      </p>
    </form>
  );
};
