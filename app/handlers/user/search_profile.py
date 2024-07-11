from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from app.keyboards.default.choise import search_kb
from app.keyboards.inline.search import check_like_ikb

from database.service.profile import elastic_search_user_ids, get_profile
from app.states.search_state import Search


@dp.message_handler(Text("🔍"))
async def _search_command(message: types.Message, state: FSMContext):
    await message.answer("Идет поиск...",reply_markup= search_kb())
    async with state.proxy() as data:
        # try:
        ids = (await elastic_search_user_ids(message.from_user.id))
        from random import shuffle
        shuffle(ids)
        data["ids"] = ids
        data["index"] = 0
    await _search_profile(message=message, state=state)
    await Search.search.set()
        # except:
    # await message.answer("Сейчас нет подходящих анкет")

@dp.message_handler(Text(["❤️","👎"]), state=Search.search)
async def _search_profile(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if ids:
            await message.answer('Анкеты закончились')
        ids = data['ids']        
        profile = await get_profile(ids[0])
        data["ids"] = ids.pop(0)
        
        if message.text == "❤️":
            index = data['index']
            await bot.send_message(
                chat_id=ids[index-1],
                text="Кому-то понравилась ваша анкета, хотите посмотреть?",
                reply_markup=check_like_ikb(message.from_user.id)
                )
        
        await send_profile(message, profile)

async def send_profile(message: types.Message, profile):
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=profile.photo,
        caption=f"{profile.name}, {profile.age}, {profile.city}\n{profile.description}",
    )

@dp.message_handler(Text("💤"), state=Search.search)
async def exit_search_profile(message: types.Message, state: FSMContext):
    await message.answer("Вы вышли из поиска")
    await state.finish()

@dp.callback_query_handler(Text(startswith="check_"))
@dp.callback_query_handler(Text(startswith="check_"), state=Search.search)
async def like_profile(callback: types.CallbackQuery, state: FSMContext):
    user_who_liked = int(callback.data.replace("check_", ""))
    profile = await get_profile(user_who_liked)

    await callback.answer('')
    await bot.send_photo(
        chat_id=callback.from_user.id,
        photo=profile.photo,
        caption=f"{profile.name}, {profile.age}, {profile.city}\n{profile.description}\n <a href='tg://user?id={user_who_liked}'>*телеграм</a>",
    )
