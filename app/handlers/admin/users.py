from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import dp

from app.filters.admin import IsAdmin
from app.handlers.msg_text import msg_text

from app.keyboards.default.admin import user_ban_or_unban_kb

@dp.message_handler(IsAdmin(), Text("👤 Пользователи"))
async def _users_admin_panel(message: types.Message) -> None:
    """Админ панель управление пользователями"""
    await message.answer(msg_text.USER_PANEL, reply_markup=user_ban_or_unban_kb())
    
@dp.message_handler(IsAdmin(), Text("⚔️ Забанить пользователей"))
async def _ban_users_command(message: types.Message) -> None:
    """Запрашивает список пользоветелей которых нужно заблокировать"""
    await message.answer(msg_text.BAN_USERS)
    
@dp.message_handler(IsAdmin(), Text("💊 Разбанить пользователей"))
async def _unban_users_commad(message: types.Message) -> None:
    """Запрашивает список пользоветелей которых нужно разблокировать"""
    await message.answer(msg_text.UNBAN_USERS)
    
"""unfinished"""
