from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import InputFile

from keyboards.inline.my_locKeyboard import keys
from loader import dp, bot


@dp.message_handler(Command("bolnitsy"))
async def send(message: types.Message):
    await message.reply(text="Joylashuvni yuboring", reply_markup=keys)
