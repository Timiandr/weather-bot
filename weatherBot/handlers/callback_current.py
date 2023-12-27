import logging

from aiogram import Router, F, types

from weatherBot.helper import get_msg_from_raw_weather_data
from weatherBot.openweathermap_api import Weather

callback_current_router = Router()
logger = logging.getLogger('TGBot')


@callback_current_router.callback_query(F.data.contains("current"))
async def command_start_handler(callback: types.CallbackQuery) -> None:
    city = callback.data.split('_')[1]
    weather = Weather(city).get()
    msg = get_msg_from_raw_weather_data(weather, city)
    await callback.message.answer(msg, parse_mode='HTML')
    await callback.message.delete()
