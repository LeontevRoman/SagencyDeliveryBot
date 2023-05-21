from aiogram import Router


def setup_routers() -> Router:
    from . import keyboard_function, join_in_group, commands_bot, commands_chat
    router = Router()
    router.include_router(keyboard_function.router)
    router.include_router(join_in_group.router)
    router.include_router(commands_bot.router)
    router.include_router(commands_chat.router)

    return router