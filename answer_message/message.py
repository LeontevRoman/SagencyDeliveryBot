from aiogram.types import ReplyKeyboardMarkup

from config import GROUP_NAME
from keyboards.keyboards import keyboard_start


async def get_command_start():
    return 'За каждого приглашенного участника группы, ты получаешь бонус 1% скидки на нашу продукцию. Максимальная скидка может достигать 20% ✔\n' \
           '\n' \
           '❗Любишь скидки - жми Пригласить друга 🔝\n' \
           '❓Сколько у тебя накопилось - жми Узнать скидку 👍🏻\n' \
           '\n' \
           'В Меню слева внизу ты найдешь всю информацию о нас💋'

async def get_command_catalog():
    return '🔻Каталог🔻\nhttps://wa.me/c/79283215667'

async def get_command_contacts():
    return '☎ Наши контакты\n+79283215667 Александр\n+79283213301 Оксана'

async def get_command_address():
    return '📍 Наш адрес\nhttps://yandex.ru/maps/org/magazin_dlya_sadovodov/12336510745'

async def get_error():
    return f'⛔ Сообщения, фото и т.п. я не принимаю! Выбери команду из Меню или задай свой вопрос в группе: {GROUP_NAME}'

async def get_chat_error():
    return '⛔ Команды в общей группе запрещены. Но их принимает наш бот - @SagencyDeliveryBot. Отправляй команды ему!'

async def user_not_in_group(message, bot):
    keyboard_view = ReplyKeyboardMarkup(keyboard=keyboard_start, resize_keyboard=True)
    await bot.send_message(chat_id=message.chat.id,
                           text=f"⛔ Чтобы начать взаимодействовать со мной:\n"
                                f"Вступи в группу 👉🏻 {GROUP_NAME}\n"
                                f"Затем пеши мне /start",
                        reply_markup=keyboard_view)
