from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import CommandStart

from loader import dp, bot
from app.keyboards.default import  base_kb, menu_kb
from database.service.profile import is_profile
from database.service.users import new_referral

hello_text = """
Привет! 👋

Добро пожаловать в наш Telegram-бот для знакомств! 💬 Чтобы начать, тебе нужно создать свой профиль. Напиши команду /create или просто нажми на неё. 🚀

Создай профиль и начни знакомиться с новыми людьми прямо сейчас!
"""

@dp.message_handler(CommandStart())
async def _start_command(message: types.Message):
    if await is_profile(message.from_user.id):
        await message.answer(
            text=("🔍 Искать анкеты \n👤 Мой профиль \n\n✉️ Пригласить друзей \n"),
            reply_markup=menu_kb(),

        )
    else:
        args = message.get_args()
        # if args:
        #     new_referral(message.from_user.id, args)
        from data.config import DIR
        with open(f'{DIR}/photo/logo.jpg', "rb") as photo:
        
            await message.answer_photo(
                photo=photo,
                caption=(hello_text),
                reply_markup=base_kb(),
            )
