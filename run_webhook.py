import asyncio
import logging

from aiohttp import web
from aiogram import Bot, Dispatcher
#from aiogram.client.telegram import TelegramAPIServer
from aiogram.webhook.aiohttp_server import SimpleRequestHandler

from config import TOKEN, WEBHOOK_DOMAIN, WEBHOOK_PATH, APP_HOST, APP_PORT
from handlers import setup_routers


async def main():
    # Настройка логирования в stdout
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )

    bot = Bot(token=TOKEN, parse_mode="HTML")
    dp = Dispatcher()
    router = setup_routers()
    dp.include_router(router)

    try:
        aiohttp_logger = logging.getLogger("aiohttp.access")
        aiohttp_logger.setLevel(logging.CRITICAL)

        # Установка вебхука
        await bot.set_webhook(
            url=WEBHOOK_DOMAIN + WEBHOOK_PATH,
            drop_pending_updates=True,
            allowed_updates=dp.resolve_used_update_types()
        )

        # Создание запуска aiohttp
        app = web.Application()
        SimpleRequestHandler(dispatcher=dp, bot=bot).register(app, path=WEBHOOK_PATH)
        runner = web.AppRunner(app)
        await runner.setup()
        site = web.TCPSite(runner, host=APP_HOST, port=APP_PORT)
        await site.start()

        print('Бот вышел в сеть...')

        # Бесконечный цикл
        await asyncio.Event().wait()
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())