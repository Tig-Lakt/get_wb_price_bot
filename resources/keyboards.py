from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


# клавиатура пользователя
btn_get_price = InlineKeyboardButton(text='Узнать цену', callback_data='get_price')

users_inline_btns = [
    btn_get_price,
]

users_inline_kb = InlineKeyboardBuilder()
users_inline_kb.add(*users_inline_btns)