import asyncio
import logging

from aiogram import Dispatcher, Bot
from config import TEST_TOKEN
from handlers import setup_routers


async def run_bot():
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=TEST_TOKEN, parse_mode="HTML")
    dp = Dispatcher()

    router = setup_routers()
    dp.include_router(router)

    print('Бот вышел в сеть...')

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == '__main__':
    asyncio.run(run_bot())
