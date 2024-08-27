from aiogram import types, F, Bot
from core.keyboards.reply import start_btn

async def get_start(message: types.Message, bot: Bot):
    text = f"Assalomu alaykum👋 <a href='tg://user?id={message.from_user.id}'>{message.from_user.full_name}</a>\nIT Akademy botiga xush kelibsiz!😊"

    await message.answer(text=text, reply_markup=start_btn)

async def textfilters(message: types.Message, bot: Bot):
    text = f"Faqtgina tugmalardan foydalanishingiz mumkin!"

    await message.answer(text=text)


async def location_uchkoprik(message: types.Message, bot: Bot):
    latitude = 40.54389153745935
    longitude = 71.06125172895626

    await message.answer("Bizning Uchko'prikdagi Manzilimiz: 📍")
    await bot.send_location(chat_id=message.chat.id, latitude=latitude, longitude=longitude)


async def location_Yangikurgan(message: types.Message, bot: Bot):
    latitude = 40.56153501913725
    longitude = 71.1416586669115

    await message.answer("Bizning Yangiqo'rg'ondagi Manzilimiz: 📍")
    await bot.send_location(chat_id=message.chat.id, latitude=latitude, longitude=longitude)