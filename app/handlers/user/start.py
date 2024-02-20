from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import CommandStart

from loader import dp, bot
from app.keyboards import base_selection, base_kb
from database.service.users import find_user


@dp.message_handler(CommandStart())
async def start_command(message: types.Message):
    db_us_id = await find_user(message.from_user.id)
    if not db_us_id:
        await message.answer(
            text=("Привет, теперь давай создадим тебе профиль! Для создание нажми или напиши '/create'"),
            reply_markup=base_kb(),
        )
    else:
        await message.answer(
            text=("🔍 Искать анкеты \n👤 Мой профиль \n❌ Удалить профиль \n✉️ Пригласить друзей \n"),
            reply_markup=base_selection(),
        )
