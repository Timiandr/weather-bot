import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.storage.memory import MemoryStorage

from config import TG_TOKEN, notify_timeout
from database import Database
from weatherBot.helper import get_msg_from_raw_weather_data
from weatherBot.openweathermap_api import Weather

bot = Bot(TG_TOKEN, parse_mode=ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
database = Database('notify.db')
logger = logging.getLogger('TGBot')


class Form(StatesGroup):
    city = State()


async def notify():
    while 1:
        await asyncio.sleep(notify_timeout)
        logger.info("Notify started!")
        users_data = database.get_users()
        for user_data in users_data:
            user_id = user_data[0]
            city = user_data[1]
            weather = Weather(city).get()
            msg = get_msg_from_raw_weather_data(weather, city)
            await bot.send_message(user_id, msg)
        logger.info("Notify users was stopped!")
