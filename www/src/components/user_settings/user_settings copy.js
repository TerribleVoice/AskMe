//import './style.css';

export default function User_Settings_Copy(props) {
    return (
    <body class="us_body">
        <div class="Layout_layout_e7uEn Layout_monochrome_T6NVz">
            <div class="Layout_content_DHSAI">
                <div class="Settings_wrapper_GH7yH">
                    <aside class="Settings_menu_FKyWy">
                        <nav class="AsideTabs_wrapper__I8NM">
                            <a id="profile" class="TabItem_container_VSqU9 undefined TabItem_active_lXfvy active" href="/app/settings/edit" aria-current="page"><span class="Icon_block_Hvwi5 TabItem_icon_FVk_2"></span>Профиль</a>
                            <a id="privacy" class="TabItem_container_VSqU9" href="/app/settings/privacy"><span class="Icon_block_Hvwi5 TabItem_icon_FVk_2"></span>Приватность</a>
                            <a id="subscriptions" class="TabItem_container_VSqU9" href="/app/settings/subscriptions"><span class="Icon_block_Hvwi5 TabItem_icon_FVk_2"></span>Подписки</a>
                            <a id="notifications" class="TabItem_container_VSqU9" href="/app/settings/notifications"><span class="Icon_block_Hvwi5 TabItem_icon_FVk_2"></span>Уведомления</a>
                            <a id="externalApps" class="TabItem_container_VSqU9" href="/app/settings/external-apps"><span class="Icon_block_Hvwi5 TabItem_icon_FVk_2"></span>Подключенные приложения</a>
                            <a id="blacklist" class="TabItem_container_VSqU9" href="/app/settings/blacklist"><span class="Icon_block_Hvwi5 TabItem_icon_FVk_2"></span>Чёрный список</a>
                        </nav>
                    </aside>
                    <div class="Settings_contentContainer_CVL6Y">
                        <h2 class="Settings_title_sAREq">Профиль</h2>
                        <div class="SettingsEdit_container_ycz84">
                            <form class="SettingsEdit_form_EEYht">
                                <div class="SettingsEdit_photoBlock_iom21">
                                    <div class="SettingsEdit_blockTitle_lMypl">Фотография профиля</div>
                                    <div class="SettingsEdit_photoFieldContainer_rHg3Z">
                                        <div class="SettingsEditPhotoField_photo_DEj6F">
                                            <div class="SettingsEditPhotoPreview_centredBox_mNKUc" style="width: 225px; height: 280px;"><img class="SettingsEditPhotoPreview_image_NVmL8" src="https://images.boosty.to/user/14032845/avatar?change_time=1682259764&amp;croped=1&amp;mh=560&amp;mw=450" style="width: 225px; height: 280px;"></img></div>
                                        </div>
                                        <div class="SettingsEditPhotoField_upload_OiNqw">
                                            <div class="SettingsEditPhotoField_buttonWrapper_FMHFl">
                                                <div class="CirclesAnimation_wrapper_BLZ9e">
                                                    <div class="CirclesAnimation_content_Dfcn9">
                                                        <div class="FileButton_container_S5fmr">
                                                            <label for="myFile" class="FileButton_label_wRR_W">
                                                                <input accept="image/*" class="FileButton_input__fX_o" id="myFile" name="photo" type="file"></input>
                                                                <span class="Icon_block_Hvwi5 FileButton_icon_Owzfl"></span>
                                                                <span class="FileButton_text_sAKVP">Выбрать файл</span>
                                                            </label>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="FileDescription_container__GxKK SettingsEditPhotoField_fileDescription_Wfpmg">PNG, JPG размером 225x280 не более 10 Mb.</div>
                                        </div>
                                    </div>
                                </div>
                                <div class="Form_standard_f_1gD">
                                    <label class="Label_label_jOBgY">Имя</label>
                                    <div class="Input_inputContainer_lPXgf">
                                        <input class="InputField_inputField_vzhmi" name="name" placeholder="Ваше имя" type="text" value="Snow-Melon"></input>
                                    </div>
                                    <div class="Input_descriptionBottomCaption_Nh7D_"><span>Имя будет показываться на вашей странице</span></div>
                                </div>
                                <div class="Form_standard_f_1gD">
                                    <span class="SettingsEditPhoneField_label_VrC8H">Номер телефона</span>
                                    <div class="SettingsEditPhoneField_container_T4BnJ">
                                        <button type="button" name="phone" class="LinkButton_button_LwwDl SettingsEditPhoneField_button_uwOfF"><span class="Icon_block_Hvwi5 SettingsEditPhoneField_icon_oVqRB"></span>Добавить номер телефона</button>
                                    </div>
                                </div>
                                <div class="Form_standard_f_1gD">
                                    <div class="Input_container_M2APT">
                                        <label class="Label_label_jOBgY">E-mail</label>
                                        <div class="Input_inputContainer_lPXgf"><input class="InputField_inputField_vzhmi" disabled="" name="email" placeholder="Ваша почта" type="text" value="mr.kozlov.09@gmail.com"><div class="Input_rightElement_UfudP"><button class="InlineButton_inlineBtn_YwyQe" type="button">Изменить</button></div></input></div>
                                        <div class="Input_descriptionBottomCaption_Nh7D_"><span>Используется для получения уведомления, нельзя использовать для входа в аккаунт</span></div>
                                    </div>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </body>
    )
};