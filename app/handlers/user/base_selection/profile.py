from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import dp, bot
from app.keyboards.keyboard import comm_profile
from database.service.users import get_profile


@dp.message_handler(Text("👤"))
async def profile_comm(message: types.Message):
    profile = await get_profile(message.from_user.id)
    # print(profile)
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=profile['photo'],
        caption=f"{profile['name']}, {profile['age']}, {profile['city']}\n{profile['description']}",
    )
    await message.answer(
        """
🔄 Заполнить профиль заново
❌ Удалить анкету
🔍 Смотреть анкеты
        """,
        reply_markup=comm_profile(),
    )



