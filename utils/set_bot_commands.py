from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Botni ishga tushurish"),
            types.BotCommand("masjid", "Eng yaqin masjidni topish"),
            types.BotCommand("dasturchi", "Dasturchi bilan bog'lanish: @BBuz_oniyo"),
            types.BotCommand("help", "Yordam"),
        ]
    )
