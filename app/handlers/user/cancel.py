from aiogram import F, types
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram.filters.state import StateFilter

from app.routers import user_router as router



from app.handlers.bot_utils import menu
@router.message(F.text == "💤", StateFilter("*"))
@router.message(Command("cancel"), StateFilter("*"))
async def cancel_command(message: types.Message, state: FSMContext) -> None:
    """Сбрасывает состояния и дает пользователю меню"""
    if state is None:
        return
    await state.clear()
    await menu(message.from_user.id)