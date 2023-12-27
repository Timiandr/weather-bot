import logging

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

cancel_router = Router()
logger = logging.getLogger('TGBot')


@cancel_router.message(Command("cancel"))
@cancel_router.message(F.text.casefold() == "cancel")
async def command_start_handler(message: Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    if current_state is None:
        return

    logger.debug(f"User {message.from_user.username}({message.from_user.id}) cancelling state {current_state}")
    await state.clear()
    await message.answer("Ввод отменён! Начать заново - /start")
