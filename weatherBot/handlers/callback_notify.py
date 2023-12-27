import logging

from aiogram import Router, F, types

from config import notify_timeout, max_notify_cities_for_user
from weatherBot.bot import database

callback_notify_router = Router()
logger = logging.getLogger('TGBot')


@callback_notify_router.callback_query(F.data.contains("notify"))
async def command_start_handler(callback: types.CallbackQuery) -> None:
    city = callback.data.split('_')[1]
    user_id = callback.from_user.id
    user_notify_cities = database.get_cities(user_id)
    if len(user_notify_cities) >= max_notify_cities_for_user:
        await callback.message.answer("Лимит городов подключаемых к уведомлениям превышен!")
    elif city in user_notify_cities:
        await callback.message.answer("Вы уже получаете уведомления по этому городу")
    else:
        database.add(user_id, city)
        msg = f"Вы включили уведомления, бот будет отправлять вам уведомления каждые <b>{notify_timeout}</b> секунд!"
        await callback.message.answer(msg)
    await callback.message.delete()
