from aiogram import Router, types, Bot, F

from config import GROUP_NAME
from filters.user_group_filter import UserNotInGroupFilter
from keyboards.keyboards import keyboard_start

router = Router()
router.message.filter(
    UserNotInGroupFilter()
)


@router.message(F.content_type != 'left_chat_member')
async def error(message: types.Message, bot=Bot):
    await message.reply(text=f"⛔ Чтобы начать взаимодействовать со мной:\n"
                             f"Вступи в группу 👉🏻 {GROUP_NAME}\n"
                             f"Затем пеши мне /start",
                        reply_markup=keyboard_start)
    await bot.delete_message(message.chat.id, message.message_id)
