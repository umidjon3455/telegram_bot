from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

keys = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🕌Eng yaqin masjid topish", callback_data="mylocation"),
        ],
])