from aiogram.fsm.state import StatesGroup, State


class UserData(StatesGroup):
    """
    FSM для обработки ввода данных пользователя.

    Состояния:
        sample (State): Ожидание ввода ....
    """
    product_article = State()