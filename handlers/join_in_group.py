from aiogram import Router, Bot, F, types
from aiogram.filters import ChatMemberUpdatedFilter, JOIN_TRANSITION


from config import db, GROUP_NAME
from filters.except_filters import except_event

router = Router()

@router.chat_member(ChatMemberUpdatedFilter(JOIN_TRANSITION))
async def handler_new_member(event: types.ChatMemberUpdated, bot: Bot):
    try:
        if event.invite_link:
            referer_id = int(event.invite_link.name) # get id referer from name invite link as int

            new_amount_invite_friends = db.update_percent_sale(referer_id) # add 1 point referer and return new value
            if new_amount_invite_friends < 20:
                await bot.send_message(event.invite_link.name,
                                       f'По твоей ссылке вступил твой друг {event.from_user.first_name}. Тебе добавлен 1% скидки!\n'
                                       f'Твоя текущая скидка - {new_amount_invite_friends}%.')
            elif new_amount_invite_friends == 20:
                await bot.send_message(event.invite_link.name,
                                       f'По твоей ссылке вступил твой друг {event.from_user.first_name}. Тебе добавлен 1% скидки!\n'
                                       f'Теперь у тебя максимальная скидка - {new_amount_invite_friends}%.')
            else:
                await bot.send_message(event.invite_link.name,
                                       f'По твоей ссылке вступил твой друг {event.from_user.first_name}.\n'
                                       f'У тебя максимальная скидка - 20%!')
        else:
            db.create_user(
                user_id = event.from_user.id,
                user_name = event.from_user.first_name)
    except:
        await except_event(bot)


@router.chat_member(ChatMemberUpdatedFilter(~JOIN_TRANSITION))
async def handler_left_member(event: types.ChatMemberUpdated, bot: Bot):
    try:
        new_amount_invite_friends, referer_id = db.down_percent_sale(event.from_user.id)

        if new_amount_invite_friends:
            if new_amount_invite_friends < 20:
                await bot.send_message(referer_id,
                                       f'Твой друг {event.from_user.first_name}, которого ты приглашал(а), покинул группу {GROUP_NAME}.\n'
                                       f'Теперь твоя скидка - {new_amount_invite_friends}%!')
            else:
                await bot.send_message(referer_id,
                                       f'Твой друг {event.from_user.first_name}, которого ты приглашал(а), покинул группу {GROUP_NAME}.\n'
                                       f'У тебя все еще максимальная скидка 20%!')
        else:
            pass
    except:
        await except_event(bot)


@router.message((F.content_type == 'new_chat_members') | (F.content_type == 'left_chat_member'))
async def delete_system_message(message: types.Message, bot: Bot):
    await bot.delete_message(message.chat.id, message.message_id)