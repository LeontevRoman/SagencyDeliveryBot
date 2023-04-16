
async def except_filter(message, bot):
    await message.answer('Что-то пошло не так. Ошибку уже отправили разработчикам. В ближайшее время все починят!')
    await bot.send_message(chat_id=782219228, text='Бот сломался нахрен - надо разобраться!')

async def except_event(bot):
    await bot.send_message(chat_id=782219228, text='Удалился пользователь которого нет в БД')