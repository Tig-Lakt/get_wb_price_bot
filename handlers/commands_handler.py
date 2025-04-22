from aiogram import types
from aiogram.filters.command import Command
from aiogram import Router

from resources import (
    users_inline_kb,
    welcome_text,
)


router = Router()


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    """
    Обработчик команды '/start'.

    Приветствует пользователя и предлагает ввести артикул.
    """
    
    await message.answer(
        text=welcome_text,
        reply_markup=users_inline_kb.as_markup(resize_keyboard=True)
        )