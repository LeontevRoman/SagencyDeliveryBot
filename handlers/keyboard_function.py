from aiogram import types, Router, Bot
from aiogram.filters import Text

from config import db, GROUP_NAME
from filters.bot_chat_filter import BotChatFilter
from filters.user_group_filter import UserInGroupFilterKeyboard
from filters.except_filters import except_filter

from keyboards.keyboards import keyboard_bot

router = Router()
router.message.filter(
    BotChatFilter(),
    UserInGroupFilterKeyboard()
)

@router.message(Text(contains=['Пригласить друга🔝'], ignore_case=True))
async def create_sales(message: types.Message, bot: Bot):

    try:
        invite_link = db.check_refaral_link(message.from_user.id)

        if invite_link:
            await message.answer(f'Ссылка может быть создана только 1 раз.\n'
                                 f'Твоя ссылка: {invite_link}\n'
                                 f'Отправляй ее своим друзьям и за каждого вступившего ты получишь бонус 1% скидки.\n'
                                 f'Максимальный размер скидки - 20%👆🏻\n',
                                 reply_markup=keyboard_bot)
        else:
            link = await bot.create_chat_invite_link(chat_id=GROUP_NAME, name=f'{message.from_user.id}')

            db.create_referal_link(message.from_user.id, link.invite_link)

            await message.answer(f'Твоя ссылка: {link.invite_link}\n'
                                 f'Отправь ее своим друзьям и за каждого вступившего ты получишь бонус 1% скидки.\n'
                                 f'Максимальный размер скидки - 20%👆🏻\n'
                                 f'Ссылка может быть создана только 1 раз. Не теряй ее!',
                                 reply_markup=keyboard_bot)
    except:
        await except_filter(message, bot)


@router.message(Text(contains=['Узнать скидку 👍🏻'], ignore_case=True))
async def show_sales(message: types.Message, bot=Bot):

    try:
        amount_invite_friends = db.get_percent_sale(message.from_user.id)

        if amount_invite_friends >= 0 and amount_invite_friends <= 10:
            await message.answer(f"Твоя скидка - {amount_invite_friends}%.\n"
                                 f"Приглашай большей друзей и увеличивай скидку!\n",
                                 reply_markup=keyboard_bot)
        elif amount_invite_friends >= 10 and amount_invite_friends <= 19:
            await message.answer(f"Твоя скидка - {amount_invite_friends}%.\n"
                                 f"Неплохо, но это не максимум. Приглашай большей друзей и увеличивай скидку!",
                                 reply_markup=keyboard_bot)
        else:
            await message.answer(f"У тебя максимальная скидка - 20%❗",
                                 reply_markup=keyboard_bot)
        pass
    except:
        await except_filter(message, bot)
