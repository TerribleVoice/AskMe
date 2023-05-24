from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

keyboard_start = InlineKeyboardMarkup()
keyboard_start_button1 = InlineKeyboardButton(text="Войти", callback_data="auth")
keyboard_start_button2 = InlineKeyboardButton(text="Зарегистрироваться", callback_data="register")
keyboard_start.add(keyboard_start_button1)
keyboard_start.add(keyboard_start_button2)

keyboard_auth = InlineKeyboardMarkup()
keyboard_auth_button1 = InlineKeyboardButton(text="Найти пользователя 🔎", callback_data="find_user")
keyboard_auth_button2 = InlineKeyboardButton(text="Список подписок 📃", callback_data="list_subs")
keyboard_auth_button3 = InlineKeyboardButton(text="Посты 📝", callback_data="posts")
keyboard_auth.add(keyboard_auth_button1)
keyboard_auth.add(keyboard_auth_button2)
keyboard_auth.add(keyboard_auth_button3)

# Кнопки, когда человек нашел пользователя

# Нет подписки
keyboard_search_user = InlineKeyboardMarkup()
keyboard_search_user_button1 = InlineKeyboardButton(text="Подписаться", callback_data="subscribe_user")
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

# Клавиатура для возвращения обратно при вводе пароля
keyboard_password = InlineKeyboardMarkup()
keyboard_password_return = InlineKeyboardButton(text='Вернутся на шаг назад 🚪', callback_data='exit_password')
keyboard_password.add(keyboard_password_return)

# Кнопка для прохождения авторизации снова
keyboard_auth_again = InlineKeyboardMarkup()
keyboard_auth_again_button1 = InlineKeyboardButton(text="Ввести логин и пароль снова", callback_data="auth_again")
keyboard_auth_again.add(keyboard_auth_again_button1)