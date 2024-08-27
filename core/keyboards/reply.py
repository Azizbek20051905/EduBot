from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


start_btn = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Ta'lim Yo'nalishlari🎯")],
        [KeyboardButton(text="Uchko'prik Lokatsiya📍")],
        [KeyboardButton(text="Yangiqo'rg'on Lokatsiya📍")]
    ],
    resize_keyboard=True
)

direction_btn = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="👩‍💻IT TA'LIM👨‍💻"), KeyboardButton(text="🇺🇸Ingliz tili🇬🇧")],
        [KeyboardButton(text="📈Trading Kursi📉"),KeyboardButton(text="🧮Matematika📏")],
        [KeyboardButton(text="🔙Orqaga")]
    ],
    resize_keyboard=True
)

it_courses = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="💻Kompyuter kursi💻"), KeyboardButton(text="🖼Grafik dizayn🖼")],
        [KeyboardButton(text="💾Frontend dasturlash💾")],
        [KeyboardButton(text="💾Backend dasturlash💾")],
        [KeyboardButton(text="💽Fullstack💽")],
        [KeyboardButton(text="🔙Orqaga")]
    ],
    resize_keyboard=True
)

english_degree = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Beginner😕"), KeyboardButton(text="Elementary🙂"), KeyboardButton(text="Pre-Intermediate🤨")],
        [KeyboardButton(text="Intermediate😉"), KeyboardButton(text="Upper-Intermediate😊"), KeyboardButton(text="Advanced😎")],
        [KeyboardButton(text="Bilmayman🤔")],
        [KeyboardButton(text="🔙Orqaga")]
    ],
    resize_keyboard=True
)

register_btn = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Ro'yxatdan o'tish✅")],
        [KeyboardButton(text="🔙Orqaga")]
    ],
    resize_keyboard=True
)

account_btn = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Kontakt ulashish", request_contact=True)]
    ],
    resize_keyboard=True
)

address_btn = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Uchko'prik"), KeyboardButton(text="Yangiqo'rg'on")],
        [KeyboardButton(text="🔙Orqaga")]
    ],
    resize_keyboard=True
)