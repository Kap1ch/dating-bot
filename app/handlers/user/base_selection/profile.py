from aiogram import types, Dispatcher
from loader import dp, bot
from app.keyboards import comm_profile
from database.bd import view_profile


@dp.message_handler(text="👤")
async def profile_comm(message: types.Message):
    profile = view_profile(message.from_user.id)
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=profile[3],
        caption=f"{profile[4]}, {profile[5]}, {profile[6]}\n{profile[7]}",
    )
    await message.answer(
        """
🔄 Заполнить профиль заново
❌ Удалить анкету
🔍 Смотреть анкеты
        """,
        reply_markup=comm_profile(),
    )



