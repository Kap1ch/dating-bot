from aiogram import F, types
from aiogram.filters import Command
from aiogram.filters.state import StateFilter
from aiogram.fsm.context import FSMContext

from app.handlers.bot_utils import menu
from app.others.states import LikeResponse, Mailing, Search
from app.routers import common_router

FILTER = (Search.search, LikeResponse.response, Mailing.message)


@common_router.message(StateFilter(FILTER), F.text == "💤")
@common_router.message(StateFilter(FILTER), Command("cancel"))
async def cancel_command(message: types.Message, state: FSMContext) -> None:
    """Сбрасывает состояния и отправляет меню пользователю"""
    await state.clear()
    await menu(message.from_user.id)
