from aiogram import types

from aiogram.filters import BaseFilter


class BotChatFilter(BaseFilter):
    async def __call__(self, message: types.Message):
        if message.chat.id == message.from_user.id:
            return True
        else:
            return False
