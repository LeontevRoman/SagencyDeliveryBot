from aiogram import types, Router, Bot, F
from aiogram.filters import Command

from config import db
from filters.bot_chat_filter import BotChatFilter
from filters.user_group_filter import UserInGroupFilter
from filters.except_filters import except_filter

from keyboards.keyboards import keyboard_bot
from answer_message.message import *

router = Router()
router.message.filter(
    UserInGroupFilter()
)

@router.message(Command('start'), BotChatFilter())
async def command_start(message: types.Message, bot=Bot):
    try:
        db.create_user(user_id=message.from_user.id, user_name=message.from_user.first_name)
        await message.answer(f'Привет {message.from_user.first_name} 🌱\n{await get_command_start()}',
                               reply_markup=keyboard_bot)
    except:
        await except_filter(message, bot)


@router.message(Command('catalog'), BotChatFilter())
async def command_catalog(message: types.Message, bot=Bot):
    try:
        await message.answer(await get_command_catalog(), reply_markup=keyboard_bot)
    except:
        await except_filter(message, bot)


@router.message(Command('contacts'), BotChatFilter())
async def command_contacts(message: types.Message, bot=Bot):
    try:
        await message.answer(await get_command_contacts(), reply_markup=keyboard_bot)
    except:
        await except_filter(message, bot)


@router.message(Command('address'), BotChatFilter())
async def command_address(message: types.Message, bot=Bot):
    try:
        await message.answer(await get_command_address(), reply_markup=keyboard_bot)
    except:
        await except_filter(message, bot)


@router.message((F.content_type != 'new_chat_members') & (F.content_type != 'left_chat_member'))
async def error(message=types.Message, bot=Bot):
    try:
        if message.chat.id == message.from_user.id:
            await message.answer(await get_error(), reply_markup=keyboard_bot)
    except:
        await except_filter(message, bot)
