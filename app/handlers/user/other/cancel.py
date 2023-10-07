from aiogram import types, Dispatcher
from loader import dp, bot, _
from aiogram.dispatcher import FSMContext
from app.keyboards import *


# выключение машины состояний
@dp.message_handler(commands="cancel", state="*")
async def com_cancel(message: types.message, state: FSMContext):
    if state is None:
        return
    await state.finish()
    await message.answer(_("Вы вышли с создания анкеты."))

    await message.answer(
        """
        \t🔍Смотреть анкеты
👤Моя анкета
❌Удалить анкету
✉️Пригласить друзей
        """,
        reply_markup=base_selection(),
    )
