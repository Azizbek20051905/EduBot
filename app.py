from aiogram import Bot, Dispatcher, types, F
from aiogram.enums import ParseMode
from aiogram.filters import Command
from core.settings import settings
from aiogram.client.bot import DefaultBotProperties

import asyncio
import logging

from core.handlers.basic import get_start, textfilters, location_uchkoprik, location_Yangikurgan
from core.handlers.keyboard_hand import (direction_handler, it_course_handler, english_course, computer_course,
                                         grafics_course, fullstack_course, frontend_course, backend_course,
                                         trading_course, register_handler, first_name_hand, last_name_hand,
                                         degree_hand, process_phone, Math_course, address,
                                         orqaga, orqaga2, orqaga3, orqaga4, orqaga5, orqaga6)
from core.states.states import GetStudentInfo, BackState
from core.utils.commands import set_commands

async def start_bot(bot: Bot):
    print("Bot ishga tushdi!")
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, text="Bot ishga tushdi!")



async def stop_bot(bot: Bot):
    print("Bot ishdan to'xtadi!")
    await bot.send_message(settings.bots.admin_id, text="Bot to'xtadi!")

async def start():
    bot = Bot(token=settings.bots.bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    logging.basicConfig(
        level="ERROR",
        filename="debug.log",
        # format="%(asctime)s - %(name)s - [ %(message)s ]",
        format="%(asctime)s - ERROR - %(name)s - %(filename)s:%(lineno)d - %(message)s",
        datefmt='%d-%b-%y %H:%M:%S')
    
    dp = Dispatcher()
    dp.startup.register(start_bot)

    dp.message.register(get_start, Command(commands='start'))
    dp.message.register(direction_handler, F.text == "Ta'lim Yo'nalishlari🎯")
    dp.message.register(location_uchkoprik, F.text == "Uchko'prik Lokatsiya📍")
    dp.message.register(location_Yangikurgan, F.text == "Yangiqo'rg'on Lokatsiya📍")
    dp.message.register(it_course_handler, F.text == "👩‍💻IT TA'LIM👨‍💻")
    dp.message.register(english_course, F.text == "🇺🇸Ingliz tili🇬🇧")
    dp.message.register(computer_course, F.text == "💻Kompyuter kursi💻")
    dp.message.register(frontend_course, F.text == "💾Frontend dasturlash💾")
    dp.message.register(backend_course, F.text == "💾Backend dasturlash💾")
    dp.message.register(fullstack_course, F.text == "💽Fullstack💽")
    dp.message.register(grafics_course, F.text == "🖼Grafik dizayn🖼")
    dp.message.register(trading_course, F.text == "📈Trading Kursi📉")
    dp.message.register(register_handler, F.text == "Ro'yxatdan o'tish✅")
    dp.message.register(Math_course, F.text == "🧮Matematika📏")
    dp.message.register(first_name_hand, GetStudentInfo.first_name)
    dp.message.register(last_name_hand, GetStudentInfo.last_name)
    dp.message.register(degree_hand, GetStudentInfo.degree)
    dp.message.register(process_phone, GetStudentInfo.number)
    dp.message.register(address, GetStudentInfo.address)
    dp.message.register(textfilters, F.text != "🔙Orqaga")
    dp.message.register(orqaga, F.text == "🔙Orqaga" and BackState.lvl1)
    dp.message.register(orqaga2, F.text == "🔙Orqaga" and BackState.lvl2)
    dp.message.register(orqaga3, F.text == "🔙Orqaga" and BackState.lvl3)
    dp.message.register(orqaga4, F.text == "🔙Orqaga" and BackState.lvl4)
    dp.message.register(orqaga5, F.text == "🔙Orqaga" and BackState.lvl5)
    dp.message.register(orqaga6, F.text == "🔙Orqaga" and BackState.lvl6)

    dp.shutdown.register(stop_bot)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start())

