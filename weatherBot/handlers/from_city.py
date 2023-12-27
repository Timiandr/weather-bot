import logging

from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from weatherBot.bot import Form
from weatherBot.keyboards import choice_keyboard
from weatherBot.openweathermap_api import Weather

from_city_router = Router()
logger = logging.getLogger('TGBot')


@from_city_router.message(Form.city)
async def command_start_handler(message: Message, state: FSMContext) -> None:
    city = message.text
    weather = Weather(city).get()
    match weather:
        case 0:
            await message.answer('Такого города не существует! Попробуйте ещё.')
            return
        case -1:
            await message.answer('Возникла проблема на сервере. Чиним...')
            return
    await state.clear()
    msg = f'Выберите тип прогноза погоды в городе {city}'
    await message.answer(msg, parse_mode="HTML", reply_markup=choice_keyboard(city))
