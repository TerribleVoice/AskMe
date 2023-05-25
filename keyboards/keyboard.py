from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

keyboard_start = InlineKeyboardMarkup()
keyboard_start_button1 = InlineKeyboardButton(text="Войти", callback_data="auth")
keyboard_start_button2 = InlineKeyboardButton(text="Зарегистрироваться", callback_data="register")
keyboard_start.add(keyboard_start_button1)
keyboard_start.add(keyboard_start_button2)

keyboard_auth = InlineKeyboardMarkup()
keyboard_auth_button1 = InlineKeyboardButton(text="Найти пользователя 🔎", callback_data="find_user")
keyboard_auth_button2 = InlineKeyboardButton(text="Список подписок 📃", callback_data="list_subs")
keyboard_auth_button3 = InlineKeyboardButton(text="Посты авторов📝", callback_data="posts")
keyboard_auth.add(keyboard_auth_button1)
keyboard_auth.add(keyboard_auth_button2)
keyboard_auth.add(keyboard_auth_button3)

# Кнопки, когда человек нашел пользователя

# Нет подписки
keyboard_search_user = InlineKeyboardMarkup()
keyboard_search_user_button1 = InlineKeyboardButton(text="Подписаться на пользователя", callback_data="subscribe_user")
keyboard_search_user.add(keyboard_search_user_button1)

# Есть подписка
keyboard_search_user_subscribe = InlineKeyboardMarkup()
keyboard_search_user_subscribe_button1 = InlineKeyboardButton(text="Посмотреть последние 10 постов", callback_data="last_posts")
keyboard_search_user_subscribe.add(keyboard_search_user_subscribe_button1)

# Кнопка, когда человек смотрит свои подписки
keyboard_subs = InlineKeyboardMarkup()
keyboard_subs_button1 = InlineKeyboardButton(text="Посмотреть посты 👁", callback_data="view_posts")
keyboard_subs.add(keyboard_subs_button1)

# Клавиатура для возвращения обратно при вводе логина или емайла
keyboard_login = InlineKeyboardMarkup()
keyboard_login_return = InlineKeyboardButton(text='Вернутся на шаг назад 🚪', callback_data='exit_login')
keyboard_login.add(keyboard_login_return)

keyboard_login_register = InlineKeyboardMarkup()
keyboard_login_register_return = InlineKeyboardButton(text='Вернутся на шаг назад 🚪', callback_data='exit_login_register')
keyboard_login_register.add(keyboard_login_register_return)

# Клавиатура для возвращения обратно при вводе пароля
keyboard_password = InlineKeyboardMarkup()
keyboard_password_return = InlineKeyboardButton(text='Вернутся на шаг назад 🚪', callback_data='exit_password')
keyboard_password.add(keyboard_password_return)

# Кнопка для прохождения авторизации снова
keyboard_auth_again = InlineKeyboardMarkup()
keyboard_auth_again_button1 = InlineKeyboardButton(text="Ввести логин и пароль снова", callback_data="auth_again")
keyboard_auth_again.add(keyboard_auth_again_button1)

# Клавиатура для возвращения при вводе логина при регистрации
keyboard_register_login = InlineKeyboardMarkup()
keyboard_login_return_register = InlineKeyboardButton(text='Вернутся на шаг назад 🚪', callback_data='exit_login_register')
keyboard_register_login.add(keyboard_login_return_register)

# Клавиатура для возвращения при вводе емайла при регистрации
keyboard_register_email = InlineKeyboardMarkup()
keyboard_email_return_register = InlineKeyboardButton(text='Вернутся на шаг назад 🚪', callback_data='exit_email_register')
keyboard_register_email.add(keyboard_email_return_register)

# Вход в аккаунт при вводе некоректного емайла
keyboard_email_wrong = InlineKeyboardMarkup()
keyboard_email_wrong_button1 = InlineKeyboardButton(text="Войти в свой аккаунт", callback_data="auth_email")
keyboard_email_wrong.add(keyboard_email_wrong_button1)

# Клавиатура для возвращения при вводе пароля при регистрации
keyboard_register_password = InlineKeyboardMarkup()
keyboard_password_return_register = InlineKeyboardButton(text='Вернутся на шаг назад 🚪', callback_data='exit_password_register')
keyboard_register_password.add(keyboard_password_return_register)

# Вернуться назад после подписки
keyboard_subscribe_back = InlineKeyboardMarkup()
keyboard_subscribe_back_button1 = InlineKeyboardButton(text="Вернутся на шаг назад 🚪", callback_data="subscribe_back")
keyboard_subscribe_back_button2 = InlineKeyboardButton(text="Посмотреть посты пользователя", callback_data="last_posts")
keyboard_subscribe_back.add(keyboard_subscribe_back_button2)
keyboard_subscribe_back.add(keyboard_subscribe_back_button1)