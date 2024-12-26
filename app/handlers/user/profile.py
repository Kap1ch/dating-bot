from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import dp, bot

from database.models import Profile
from database.service.profile import get_profile

from app.handlers.msg_text import msg_text
from app.keyboards.default import profile_kb

@dp.message_handler(Text("👤"))
async def _profile_command(message: types.Message) -> None:
    
    profile = await get_profile(message.from_user.id)

    await send_profile(message.from_user.id, profile)
    await message.answer(msg_text.PROFILE_MENU, reply_markup=profile_kb())


async def send_profile(user_id: int, profile: Profile) -> None:
    await bot.send_photo(
        chat_id=user_id,
        photo=profile.photo,
        caption=f"{profile.name}, {profile.age}, {profile.city}\n{profile.description}",
    )

