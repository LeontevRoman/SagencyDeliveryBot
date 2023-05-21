from aiogram import types

from aiogram.filters import BaseFilter


class GroupChatFilter(BaseFilter):
    async def __call__(self, message: types.Message):
        if message.chat.username == 'sagencydelivery':
            return True
        else:
            return False
