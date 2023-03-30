from aiogram import Router


def setup_routers() -> Router:
    from . import block_message_not_member, keyboard_function, join_in_group, commands_bot
    router = Router()
    router.include_router(block_message_not_member.router)
    router.include_router(keyboard_function.router)
    router.include_router(join_in_group.router)
    router.include_router(commands_bot.router)

    return router