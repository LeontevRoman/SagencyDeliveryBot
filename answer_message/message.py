from aiogram.types import ReplyKeyboardMarkup

from config import GROUP_NAME
from keyboards.keyboards import keyboard_start, keyboard_group


async def get_command_start():
    return 'За каждого приглашенного участника группы, ты получаешь бонус 1% скидки на нашу продукцию. Максимальная скидка может достигать 20% ✔\n' \
           '\n' \
           '❗Любишь скидки - жми Пригласить друга 🔝\n' \
           '❓Сколько у тебя накопилось - жми Узнать скидку 👍🏻\n' \
           '\n' \
           'В Меню слева внизу ты найдешь всю информацию о нас💋'

async def get_command_catalog():
    return '🔻Каталог плодовые и ягодные🔻\nhttps://wa.me/c/79283215667\n\n' \
           '🔻Каталог декоративные🔻\nhttps://wa.me/c/79283213301'

async def get_command_contacts():
    return '☎ Наши контакты\n+79283215667 Александр\n+79283213301 Оксана'

async def get_command_address():
    return '📍 Наш адрес\nhttps://yandex.ru/maps/org/magazin_dlya_sadovodov/12336510745'

async def get_error():
    return f'⛔ Сообщения, фото и т.п. я не принимаю! Выбери команду из Меню или задай свой вопрос в группе: {GROUP_NAME}'

async def get_chat_start_error():
    return '⛔ Команда start в общей группе не работает. Отправляй ее нашему боту - @SagencyDeliveryBot '

async def user_not_in_group():
     return f'⛔ Чтобы начать взаимодействовать со мной:\n' \
            f'Вступи в группу 👉🏻 {GROUP_NAME}\n' \
            f'Затем пеши мне /start'

async def delete_user_not_referer_id():
    return 'Удалился пользователь у которого не было реферала'