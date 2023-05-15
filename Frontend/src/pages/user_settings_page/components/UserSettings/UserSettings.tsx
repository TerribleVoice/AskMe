export const UserSettings = () => {
  return (
    <body className="container">
      <div className="Layout_layout_e7uEn Layout_monochrome_T6NVz">
        <div className="Layout_content_DHSAI">
          <div className="Settings_wrapper_GH7yH">
            <aside className="Settings_menu_FKyWy">
              <nav className="AsideTabs_wrapper__I8NM">
                <a
                  id="profile"
                  className="TabItem_container_VSqU9 undefined TabItem_active_lXfvy active"
                  href="/app/settings/edit"
                  aria-current="page"
                >
                  <span className="Icon_block_Hvwi5 TabItem_icon_FVk_2"></span>
                  Профиль
                </a>
                <a
                  id="privacy"
                  className="TabItem_container_VSqU9"
                  href="/app/settings/privacy"
                >
                  <span className="Icon_block_Hvwi5 TabItem_icon_FVk_2"></span>
                  Приватность
                </a>
                <a
                  id="subscriptions"
                  className="TabItem_container_VSqU9"
                  href="/app/settings/subscriptions"
                >
                  <span className="Icon_block_Hvwi5 TabItem_icon_FVk_2"></span>
                  Подписки
                </a>
                <a
                  id="notifications"
                  className="TabItem_container_VSqU9"
                  href="/app/settings/notifications"
                >
                  <span className="Icon_block_Hvwi5 TabItem_icon_FVk_2"></span>
                  Уведомления
                </a>
                <a
                  id="externalApps"
                  className="TabItem_container_VSqU9"
                  href="/app/settings/external-apps"
                >
                  <span className="Icon_block_Hvwi5 TabItem_icon_FVk_2"></span>
                  Подключенные приложения
                </a>
                <a
                  id="blacklist"
                  className="TabItem_container_VSqU9"
                  href="/app/settings/blacklist"
                >
                  <span className="Icon_block_Hvwi5 TabItem_icon_FVk_2"></span>
                  Чёрный список
                </a>
              </nav>
            </aside>
            <div className="Settings_contentContainer_CVL6Y">
              <h2 className="Settings_title_sAREq">Профиль</h2>
              <div className="SettingsEdit_container_ycz84">
                <form className="SettingsEdit_form_EEYht">
                  <div className="SettingsEdit_photoBlock_iom21">
                    <div className="SettingsEdit_blockTitle_lMypl">
                      Фотография профиля
                    </div>
                    <div className="SettingsEdit_photoFieldContainer_rHg3Z">
                      <div className="SettingsEditPhotoField_photo_DEj6F">
                        <div
                          className="SettingsEditPhotoPreview_centredBox_mNKUc"
                        >
                          <img
                            className="SettingsEditPhotoPreview_image_NVmL8"
                            src="https://images.boosty.to/user/14032845/avatar?change_time=1682259764&amp;croped=1&amp;mh=560&amp;mw=450"
                          ></img>
                        </div>
                      </div>
                      <div className="SettingsEditPhotoField_upload_OiNqw">
                        <div className="SettingsEditPhotoField_buttonWrapper_FMHFl">
                          <div className="CirclesAnimation_wrapper_BLZ9e">
                            <div className="CirclesAnimation_content_Dfcn9">
                              <div className="FileButton_container_S5fmr">
                                <label
                                  htmlFor="myFile"
                                  className="FileButton_label_wRR_W"
                                >
                                  <input
                                    accept="image/*"
                                    className="FileButton_input__fX_o"
                                    id="myFile"
                                    name="photo"
                                    type="file"
                                  />
                                  <span className="Icon_block_Hvwi5 FileButton_icon_Owzfl"></span>
                                  <span className="FileButton_text_sAKVP">
                                    Выбрать файл
                                  </span>
                                </label>
                              </div>
                            </div>
                          </div>
                        </div>
                        <div className="FileDescription_container__GxKK SettingsEditPhotoField_fileDescription_Wfpmg">
                          PNG, JPG размером 225x280 не более 10 Mb.
                        </div>
                      </div>
                    </div>
                  </div>
                  <div className="Form_standard_f_1gD">
                    <label className="Label_label_jOBgY">Имя</label>
                    <div className="Input_inputContainer_lPXgf">
                      <input
                        className="InputField_inputField_vzhmi"
                        name="name"
                        placeholder="Ваше имя"
                        type="text"
                        value="Snow-Melon"
                      />
                    </div>
                    <div className="Input_descriptionBottomCaption_Nh7D_">
                      <span>Имя будет показываться на вашей странице</span>
                    </div>
                  </div>
                  <div className="Form_standard_f_1gD">
                    <span className="SettingsEditPhoneField_label_VrC8H">
                      Номер телефона
                    </span>
                    <div className="SettingsEditPhoneField_container_T4BnJ">
                      <button
                        type="button"
                        name="phone"
                        className="LinkButton_button_LwwDl SettingsEditPhoneField_button_uwOfF"
                      >
                        <span className="Icon_block_Hvwi5 SettingsEditPhoneField_icon_oVqRB"></span>
                        Добавить номер телефона
                      </button>
                    </div>
                  </div>
                  <div className="Form_standard_f_1gD">
                    <div className="Input_container_M2APT">
                      <label className="Label_label_jOBgY">E-mail</label>
                      <div className="Input_inputContainer_lPXgf">
                        <input
                          className="InputField_inputField_vzhmi"
                          disabled={false}
                          name="email"
                          placeholder="Ваша почта"
                          type="text"
                          value="mr.kozlov.09@gmail.com"
                        />
                        <div className="Input_rightElement_UfudP">
                          <button
                            className="InlineButton_inlineBtn_YwyQe"
                            type="button"
                          >
                            Изменить
                          </button>
                        </div>
                      </div>
                      <div className="Input_descriptionBottomCaption_Nh7D_">
                        <span>
                          Используется для получения уведомления, нельзя
                          использовать для входа в аккаунт
                        </span>
                      </div>
                    </div>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </body>
  );
};
