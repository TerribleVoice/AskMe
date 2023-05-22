from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

keyboard_start = InlineKeyboardMarkup()
keyboard_start_button1 = InlineKeyboardButton(text="Авторизоваться ✅", callback_data="auth")
keyboard_start.add(keyboard_start_button1)