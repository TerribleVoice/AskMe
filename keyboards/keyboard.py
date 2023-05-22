from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

keyboard_start = InlineKeyboardMarkup()
keyboard_start_button1 = InlineKeyboardButton(text="Авторизоваться ✅", callback_data="auth")
keyboard_start.add(keyboard_start_button1)

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
keyboard_search_user_button1 = InlineKeyboardButton(text="Подписаться", callback_data="find_user")
keyboard_search_user.add(keyboard_search_user_button1)

# Есть подписка
keyboard_search_user_subscribe = InlineKeyboardMarkup()
keyboard_search_user_subscribe_button1 = InlineKeyboardButton(text="Посмотреть последние 10 постов", callback_data="last_posts")
keyboard_search_user_subscribe.add(keyboard_search_user_subscribe_button1)