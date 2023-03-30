import asyncio
import logging

from aiogram import Dispatcher, Bot
from config import TOKEN

from handlers import keyboard_function
from handlers import join_in_group
from handlers import commands_bot
from handlers import block_message_not_member


async def run_bot():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=TOKEN, parse_mode="HTML")
    dp = Dispatcher()

    print('Бот вышел в сеть...')

    dp.include_router(block_message_not_member.router)
    dp.include_router(keyboard_function.router)
    dp.include_router(join_in_group.router)
    dp.include_router(commands_bot.router)


    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == '__main__':
    asyncio.run(run_bot())
