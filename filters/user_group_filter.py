from aiogram import types, Bot
from aiogram.filters import BaseFilter

from answer_message.message import user_not_in_group
from config import GROUP_NAME
from keyboards.keyboards import keyboard_start


class UserInGroupFilter(BaseFilter):
    def __init__(self, user_member='left'):
        self.user_member = user_member

    async def __call__(self, message: types.Message, bot=Bot) -> bool:
        user_group_status = await bot.get_chat_member(chat_id=GROUP_NAME, user_id=message.from_user.id)

        if self.user_member != user_group_status.status:
            return True
        else:
            await message.reply(await user_not_in_group(), reply_markup=keyboard_start)
            return False

class UserInGroupFilterKeyboard(BaseFilter):
    def __init__(self, user_member='left'):
        self.user_member = user_member

    async def __call__(self, message: types.Message, bot=Bot) -> bool:
        user_group_status = await bot.get_chat_member(chat_id=GROUP_NAME, user_id=message.from_user.id)

        if self.user_member != user_group_status.status:
            return True
        else:
            return False