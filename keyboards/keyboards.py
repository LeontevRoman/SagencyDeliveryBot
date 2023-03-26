from aiogram.types import KeyboardButton as KB, ReplyKeyboardMarkup

keyboard_bot = ReplyKeyboardMarkup(
    keyboard=[[KB(text="Пригласить друга🔝"),
               KB(text="Узнать скидку 👍🏻")]],
    resize_keyboard=True)

keyboard_start = ReplyKeyboardMarkup(
    keyboard=[[KB(text="/start")]],
    resize_keyboard=True)
