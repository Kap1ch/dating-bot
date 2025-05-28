from aiogram import F, types
from aiogram.filters.state import StateFilter
from aiogram.fsm.context import FSMContext

import app.filters.create_profile_filtres as filters
from app.handlers.bot_utils import (
    complaint_to_profile,
    menu,
    send_profile_with_dist,
    send_user_like_alert,
)
from app.handlers.message_text import user_message_text as umt
from app.keyboards.default.base import cancel_mailing_to_user_kb, search_kb
from app.keyboards.default.report import report_kb
from app.others.states import Search
from app.routers import dating_router
from database.models import UserModel
from database.services import Match, Profile, User
from database.services.search import search_profiles

from ..common.cancel import cancel_command


@dating_router.message(StateFilter(None), F.text == "🔍")
async def _search_command(
    message: types.Message, state: FSMContext, user: UserModel, session
) -> None:
    """Бот подбирает анкеты, соответствующие предпочтениям пользователя, и предлагает их"""
    await message.answer(umt.SEARCH, reply_markup=search_kb)

    if profile_list := await search_profiles(session, user.profile):
        await state.set_state(Search.search)
        await state.update_data(ids=profile_list)

        another_profile = await Profile.get(session, profile_list[0])
        await send_profile_with_dist(user, another_profile)
    else:
        await message.answer(umt.INVALID_PROFILE_SEARCH)
        await menu(message.from_user.id)


@dating_router.message(
    StateFilter(Search.search),
    F.text.in_(("❤️", "👎", "💢", "📩")),
)
async def _search_profile(
    message: types.Message, state: FSMContext, user: UserModel, session
) -> None:
    """
    Пользователь может взаимодействовать с анкетами, предложенными ботом,
    ставя лайк или дизлайк.
    Также доступна функция жалобы на анкеты, содержащие нежелательный контент.
    Все жалобы отправляются в модераторскую группу, если она указана в настройках.
    """
    data = await state.get_data()
    profile_list = data.get("ids", [])
    another_user = await User.get_with_profile(session, profile_list[0])

    if message.text == "❤️":
        await like_profile(
            session=session,
            message=message,
            another_user=another_user,
        )
    elif message.text == "👎":
        pass
    elif message.text == "📩":
        await state.set_state(Search.message)
        await message.answer(umt.MAILING_TO_USER, reply_markup=cancel_mailing_to_user_kb)
        return

    if message.text == "💢":
        await message.answer(umt.COMPLAINT, reply_markup=report_kb())
        return
    await next_profile(session, message, profile_list, user, state)


@dating_router.message(StateFilter(Search.search), F.text.in_(("🔞", "💰", "🔫", "↩️")))
async def _search_profile_report(
    message: types.Message, state: FSMContext, user: UserModel, session
) -> None:
    """Пользователь может отправить жалобу на анкету, если она содержит нежелательный контент."""
    data = await state.get_data()
    profile_list = data.get("ids", [])
    another_user = await User.get_with_profile(session, profile_list[0])

    if message.text in ("🔞", "💰", "🔫"):
        await message.answer(umt.REPORT_TO_PROFILE, reply_markup=search_kb)
        await complaint_to_profile(
            complainant=user,
            reason=message.text,
            complaint_user=another_user,
        )
    elif message.text == "↩️":
        await message.answer(umt.SEARCH, reply_markup=search_kb)
    await next_profile(session, message, profile_list, user, state)


@dating_router.message(StateFilter(Search.message), F.text, filters.IsMessageToUser())
async def _search_profile_mailing_(
    message: types.Message, state: FSMContext, user: UserModel, session
) -> None:
    """Ловит сообщение которые пользователь отправляет в ответ на анкету"""
    data = await state.get_data()
    profile_list = data.get("ids", [])
    another_user = await User.get_with_profile(session, profile_list[0])
    await state.set_state(Search.search)

    if message.text == "↩️":
        await send_profile_with_dist(user, another_user.profile, keyboard=search_kb)
        return
    await like_profile(
        session=session,
        message=message,
        another_user=another_user,
        mail_text=message.text,
    )
    await next_profile(session, message, profile_list, user, state)


@dating_router.message(StateFilter(Search.message))
async def _search_profile_mailing_error(message: types.Message) -> None:
    """Ловит ошибку, если пользователь отправляет сообщение не по шаблону"""
    await message.answer(umt.INVALID_MAILING_TO_USER)


async def next_profile(
    session,
    message: types.Message,
    profile_list: UserModel,
    user: UserModel,
    state: FSMContext,
):
    profile_list.pop(0)
    if profile_list:
        profile = await Profile.get(session, profile_list[0])
        await state.update_data(ids=profile_list)
        await send_profile_with_dist(user, profile)
    else:
        await message.answer(umt.EMPTY_PROFILE_SEARCH)
        await cancel_command(message, state)


async def like_profile(
    session,
    message: types.Message,
    another_user: UserModel,
    mail_text: str | None = None,
):
    is_create = await Match.create(session, message.from_user.id, another_user.id, mail_text)

    if is_create:
        matchs_count = len(await Match.get_user_matchs(session, message.from_user.id))
        if matchs_count == 1 or matchs_count % 3 == 0:
            await send_user_like_alert(session, another_user)
