import logging

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from weatherBot.bot import Form

start_router = Router()
logger = logging.getLogger('TGBot')


@start_router.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    msg = (f"Привет, <b>{message.from_user.first_name}</b>! Я бот по прогнозам погоды.\n"
           f"Отправь мне город в котором хочешь посмотреть прогноз.")
    await message.answer(msg, parse_mode='HTML')
    await state.set_state(Form.city)
