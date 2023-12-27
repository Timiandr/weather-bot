import logging
import os

from aiogram import Router, F, types
from aiogram.types import FSInputFile

from weatherBot.bot import bot
from weatherBot.helper import create_plot_from_weather_data
from weatherBot.openweathermap_api import Weather

callback_forecast_router = Router()
logger = logging.getLogger('TGBot')


@callback_forecast_router.callback_query(F.data.contains("forecast"))
async def command_start_handler(callback: types.CallbackQuery) -> None:
    city = callback.data.split('_')[1]
    weather = Weather(city).get_forecast()
    plot_path = create_plot_from_weather_data(weather, city)
    await callback.message.answer_photo(FSInputFile(plot_path), caption=f'@{(await bot.me()).username} 😎')
    await callback.message.delete()
    if os.path.exists(plot_path): os.remove(plot_path)
