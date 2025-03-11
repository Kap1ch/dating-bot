from aiogram import F, types
from aiogram.filters.state import StateFilter
from aiogram.fsm.context import FSMContext

from app.handlers.bot_utils import menu
from app.handlers.message_text import user_message_text as umt
from app.keyboards.default.base import profile_return_kb
from app.others.states import DisableProfile, ProfileEdit
from app.routers import user_router as router
from database.models import UserModel
from database.services import Profile


@router.message(F.text == "🖼", StateFilter(None))
async def _edit_profile_photo_command(message: types.Message, state: FSMContext) -> None:
    """Редактирует фотографию пользователя"""
    await state.set_state(ProfileEdit.photo)
    await message.answer(umt.PHOTO)


@router.message(F.text == "✍️", StateFilter(None))
async def _edit_profile_description_command(message: types.Message, state: FSMContext) -> None:
    """Редактирует описание пользователя"""
    await state.set_state(ProfileEdit.desc)
    await message.answer(umt.DESCRIPTION)


@router.message(F.text == "❌", StateFilter(None))
async def _disable_profile_command(
    message: types.Message, state: FSMContext, user: UserModel, session
) -> None:
    """Отключает профиль пользователя, и не дает ему дальше пользоватся ботом до восстановления"""
    await state.set_state(DisableProfile.waiting)
    await Profile.update_isactive(session, user.profile, False)
    await message.answer(text=umt.DISABLE_PROFILE, reply_markup=profile_return_kb)


return_profile_tuple = (
    "🔙 Вернуть профиль",
    "🔙 Return profile",
    "🔙 Повернути профіль",
    "🔙 Wróć do profilu",
    "🔙 Perfil de retorno",
    "🔙 Profil de retour",
)


@router.message(F.text == "🔙", DisableProfile.waiting)
async def _activate_profile_command(
    message: types.Message, state: FSMContext, user: UserModel, session
) -> None:
    """Активирует профиль пользователя и выводит и состояния блокировки"""
    await Profile.update_isactive(session, user.profile, True)
    await message.answer(umt.ACTIVATE_PROFILE_ALERT)
    await state.clear()
    await menu(user.id)
