from aiogram import types
from aiogram.dispatcher.filters import Text


from loader import dp, bot
from database.service.profile import delete_profile
from app.keyboards.inline.profile import delete_profile_ikb 
from .profile import _profile_command

@dp.message_handler(Text("🖼"))
async def _edit_profile_photo_command(message: types.Message):
    await message.answer(
        text=("Отправте фотографию которую хотите поствить"),
    )

@dp.message_handler(Text("✍️"))
async def _edit_profile_description_command(message: types.Message):
    await message.answer(
        text=("Введите новое описание:"),
    )

@dp.message_handler(Text("❌"))
async def _delete_profile_commmand(message: types.Message):
    await message.answer(
        text=("Вы точно хотите удалить анкету?"),
        reply_markup=delete_profile_ikb(),
    )


@dp.callback_query_handler(Text(["delete_yes", "delete_no"]))
async def _delete_profile_choise(callback: types.CallbackQuery):
    if callback.data == "delete_yes":
        await delete_profile(callback.from_user.id)
        await callback.answer(text=("Ваша анкета успешно удалена."))
        await callback.message.answer("Если хотите снова создать вашу анкету напиши команду /create")
    elif callback.data == "delete_no":
        await _profile_command()

