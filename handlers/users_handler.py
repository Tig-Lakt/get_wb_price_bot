from aiogram import types
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from states import UserData

from resources import (
    price_text,
    error_text,
    chek_price_text,
    users_inline_kb,
)

from functions import get_price


router = Router()


@router.callback_query(F.data == "get_price")
async def f_get_price(callback: types.CallbackQuery, state: FSMContext): 
    """
    Обработчик кнопки 'Узнать цену'.

    Предлагает ввести артикул.
    """
    
    await callback.message.answer(
        text=price_text,
        )
    
    await state.set_state(UserData.product_article)


@router.message(UserData.product_article)
async def f_product_article(message: types.Message, state: FSMContext):
    if message.text.isdigit() == False:
        await message.answer(
        text=error_text,
        )
        await state.set_state(UserData.product_article) 
    else:
        await message.answer(
            text=chek_price_text,
            )
        
        price = await get_price(message.text)
        if price == (0, 0):
            msg = 'Артикул не найден, проверьте данные и повторите ввод.'
        else:
            msg = f'Стоимость товара <b>{price[1]}</b>, \nСоставляет {price[0]}₽' 
        
        await message.answer(
            text=msg,
            reply_markup=users_inline_kb.as_markup(resize_keyboard=True)
            )