from aiogram import types, Router, Bot, F
from aiogram.filters import Command

from filters.group_chat_filter import GroupChatFilter
from filters.except_filters import except_filter

from keyboards.keyboards import keyboard_group
from answer_message.message import *

router = Router()
router.message.filter(
    GroupChatFilter()
)

@router.message(Command('start'))
async def command_start(message: types.Message, bot=Bot):
    try:
        await message.answer(await get_chat_start_error(), reply_markup=keyboard_group)
    except:
        await except_filter(message, bot)


@router.message(Command('catalog'))
async def command_catalog(message: types.Message, bot=Bot):
    try:
        await message.answer(await get_command_catalog(), reply_markup=keyboard_group)
    except:
        await except_filter(message, bot)


@router.message(Command('contacts'))
async def command_contacts(message: types.Message, bot=Bot):
    try:
        await message.answer(await get_command_contacts(), reply_markup=keyboard_group)
    except:
        await except_filter(message, bot)


@router.message(Command('address'))
async def command_address(message: types.Message, bot=Bot):
    try:
        await message.answer(await get_command_address(), reply_markup=keyboard_group)
    except:
        await except_filter(message, bot)

