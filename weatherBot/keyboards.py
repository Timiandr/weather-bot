from aiogram import types

from aiogram.utils.keyboard import InlineKeyboardBuilder


def choice_keyboard(city: str) -> types.InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    current_btn = types.InlineKeyboardButton(text="На сегодня", callback_data=f'current_{city}')
    forecast_btn = types.InlineKeyboardButton(text="На 5 дней", callback_data=f'forecast_{city}')
    notify_btn = types.InlineKeyboardButton(text="Уведомления", callback_data=f'notify_{city}')
    builder.row(current_btn, forecast_btn)
    builder.row(notify_btn)
    return builder.as_markup()
