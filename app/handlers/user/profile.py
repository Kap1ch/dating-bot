from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import dp, bot
from app.keyboards.keyboard import comm_profile
from database.service.users import get_profile


@dp.message_handler(Text("👤"))
async def _profile_command(message: types.Message):
    user = await get_profile(message.from_user.id)
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=user.photo,
        caption=f"{user.name}, {user.age}, {user.city}\n{user.description}",
    )
    await message.answer(
        """
🔄 Заполнить анкету заново
🖼 Изменить фотографию
✍️ Изменить описание
❌ Удалить анкету
🔍 Смотреть анкеты
        """,
        reply_markup=comm_profile(),
    )



