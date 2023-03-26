from aiogram import types

from aiogram.filters import BaseFilter

from answer_message.message import get_chat_error


class BotChatFilter(BaseFilter):
    async def __call__(self, message: types.Message):
        if message.chat.id == message.from_user.id:
            return True
        else:
            await message.answer(await get_chat_error())
            return False