from aiogram import types, F, Bot
from aiogram.fsm.context import FSMContext
from core.states.states import BackState, GetStudentInfo
from core.keyboards.reply import direction_btn, it_courses, register_btn, english_degree, account_btn, start_btn, address_btn
from core.settings import settings
import datetime

# Ta'lim Yo'nalishlari
async def direction_handler(message: types.Message, state: FSMContext):
    await state.set_state(BackState.lvl5)  
    await message.answer("O'zingizga tegishli kursni tanlang: ", reply_markup=direction_btn)

# IT TA'LIM
async def it_course_handler(message: types.Message, state: FSMContext):
    await state.set_state(BackState.lvl4)
    await message.answer("IT Yo'nalishidan qaysi birida o'qimoqchisiz! ", reply_markup=it_courses)

# Chet Tillari
async def english_course(message: types.Message, state: FSMContext):
    await state.update_data(course = "Ingliz Tili")
    await state.set_state(BackState.lvl4)
    await message.answer("Ingliz tili: \n\nIELTS,\nCEFR,\nGRAMATIKA bo'yicha darslar.\nTo'liq malumotni adminlarimizdan bilib olishingiz mumkin!✅", reply_markup=register_btn)

async def computer_course(message: types.Message, state: FSMContext):
    await state.update_data(course = "Kompyuter kursi")
    await state.set_state(BackState.lvl3)
    await message.answer("Kompyuter kursi: \n\nWord,\nExcel,\nPowerpoint,\nMovavi darslari o'tiladi!\nTo'liq malumotni batafsil operatorlarimizdan bilib olishingiz mumkin!✅", reply_markup=register_btn)

async def grafics_course(message: types.Message, state: FSMContext):
    await state.update_data(course = "Grafik dizayn")
    await state.set_state(BackState.lvl3)
    await message.answer("Grafik dizayn: \n\nPhotoshop,\nCorel Draw,\nAdobe Illustrator bo'yicha darslar bo'ladi! \nTo'liq malumotni batafsil operatorlarimizdan bilib olishingiz mumkin!✅", reply_markup=register_btn)

async def fullstack_course(message: types.Message, state: FSMContext):
    await state.update_data(course = "Fullstack")
    await state.set_state(BackState.lvl3)
    await message.answer("Fullstack: \n\nFrontend va Backend bo'yicha darslar bo'ladi! \nTo'liq malumotni batafsil operatorlarimizdan bilib olishingiz mumkin!✅", reply_markup=register_btn)

async def frontend_course(message: types.Message, state: FSMContext):
    await state.update_data(course = "Frontend")
    await state.set_state(BackState.lvl3)
    await message.answer("Frontend: \n\nHtml,\nCss,\nBootstrap,\nSASS,\nJavascript bo'yicha darslar o'tiladi! \nTo'liq malumotni batafsil operatorlarimizdan bilib olishingiz mumkin!✅", reply_markup=register_btn)

async def backend_course(message: types.Message, state: FSMContext):
    await state.update_data(course = "Backend")
    await state.set_state(BackState.lvl3)
    await message.answer("Backend: \n\nPython,\nTelegram bot,\nDjango bo'yicha darslar o'tiladi! \nTo'liq malumotni batafsil operatorlarimizdan bilib olishingiz mumkin!✅", reply_markup=register_btn)


async def trading_course(message: types.Message, state: FSMContext):
    await state.update_data(course = "Trading")
    await state.set_state(BackState.lvl4)
    await message.answer("Trading: \n\nICT Strategiyasi bo'yicha darslar o'tiladi! \nTo'liq malumotni batafsil operatorlarimizdan bilib olishingiz mumkin!✅", reply_markup=register_btn)

async def Math_course(message: types.Message, state: FSMContext):
    await state.update_data(course = "Matematika")
    await state.set_state(BackState.lvl4)
    await message.answer("Matematika: \n\nMatematika fanidan sifatli ta'lim Oling \nTo'liq malumotni batafsil operatorlarimizdan bilib olishingiz mumkin!✅", reply_markup=register_btn)


# # Orqaga lvl1
async def orqaga(message: types.Message, state: FSMContext):
    await state.set_state(BackState.lvl6)
    print("orqaga1 lvl6")
    await message.answer("🔙 Orqaga", reply_markup=direction_btn)


async def orqaga2(message: types.Message, state: FSMContext):
    await state.set_state(BackState.lvl1)
    print("orqaga2 lvl1")
    await message.answer("🔙 Orqaga", reply_markup=it_courses)


async def orqaga3(message: types.Message, state : FSMContext):
    await state.set_state(BackState.lvl5)
    print("orqaga3 lvl5")
    await message.answer("🔙 Orqaga", reply_markup=direction_btn)


async def orqaga4(message: types.Message, state: FSMContext):
    await state.set_state(BackState.lvl6)
    print("orqaga4 lvl1")
    await message.answer("🔙 Orqaga", reply_markup=direction_btn)


async def orqaga5(message: types.Message):
    print("orqaga5 non")
    await message.answer("🔙 Orqaga", reply_markup=start_btn)  

async def orqaga6(message : types.Message):
    print("orqaga6 non")
    await message.answer("🔙 Orqaga", reply_markup=start_btn)



# "Ro'yxatdan o'tish"
async def register_handler(message: types.Message, state: FSMContext):
    await message.answer("Ismingizni kiriting:")
    await state.set_state(GetStudentInfo.first_name)

async def first_name_hand(message: types.Message, state: FSMContext):
    if message.text == "🔙Orqaga":
        await message.answer("🔙 Orqaga", reply_markup=direction_btn)
        await state.clear()
        print("if")
    else:
        print("Else")
        await state.update_data(first_name=message.text)
        await message.answer("Familiyangizni kiriting:")
        await state.set_state(GetStudentInfo.last_name)

    
async def last_name_hand(message: types.Message, state: FSMContext):
    if message.text == "🔙Orqaga":
        await message.answer("🔙 Orqaga", reply_markup=direction_btn)
        await state.clear()
    else:
        data = await state.get_data()
        await state.update_data(last_name=message.text)
        
        if data.get("course") == "Ingliz Tili":
            await message.answer("Darajangizni tanlang: ", reply_markup=english_degree)
            await state.set_state(GetStudentInfo.degree)
        else:
            await message.answer("Telefon raqamingizni kiriting:\nMasalan: (998 XX XXX XX XX)", reply_markup=account_btn)
            await state.set_state(GetStudentInfo.number)

async def degree_hand(message: types.Message, state: FSMContext):
    if message.text == "🔙Orqaga":
        await message.answer("🔙 Orqaga", reply_markup=direction_btn)
        await state.clear()
    else:
        await state.update_data(degree=message.text)
        await message.answer("Telefon raqamingizni kiriting:", reply_markup=account_btn)
        await state.set_state(GetStudentInfo.number)

async def process_phone(message: types.Message, state: FSMContext):
    if message.text == "🔙Orqaga":
        await message.answer("🔙 Orqaga", reply_markup=direction_btn)
        await state.clear()
    else:
        if message.text:
            phone = message.text
        else:
            phone = message.contact.phone_number
        
        await state.update_data(number = phone)
        await message.answer("Sizga qayerda o'qish qulay:", reply_markup=address_btn)
        await state.set_state(GetStudentInfo.address)


async def address(message: types.Message, state: FSMContext):
    if message.text == "🔙Orqaga":
        await message.answer("🔙 Orqaga", reply_markup=direction_btn)
        await state.clear()
    else:
        user_data = await state.get_data()
        first_name = user_data.get('first_name')
        last_name = user_data.get('last_name')
        phone = user_data.get('number')
        
        address = message.text
        if address == "Uchko'prik":
            await message.answer("Bizning Uchko'prikdagi Manzilimiz: 📍")
            await message.bot.send_location(chat_id=message.chat.id, latitude=40.54389153745935, longitude=71.06125172895626)
        else:
            await message.answer("Bizning Yangiqo'rg'ondagi Manzilimiz: 📍")
            await message.bot.send_location(chat_id=message.chat.id, latitude=40.56153501913725, longitude=71.1416586669115)

        course = user_data.get('course')
        date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        admin_id = settings.bots.admin_id
        admin_dilbek = 6640737881

        if course == "Ingliz Tili":
            degree = user_data.get('degree')
            await message.bot.send_message(admin_id, text=f"Yangi ro'yxatdan o'tish:\n\nIsm: <b>{first_name}</b>\nFamiliya: <b>{last_name}</b>\nTelefon: <b>{phone}</b>\nManzil: <b>{address}</b>\nKurs: <b>{course}</b>\nDaraja: <b>{degree}</b>\n\n📅{date}")
            await message.bot.send_message(message.from_user.id,"Adminlar siz bilan aloqaga chiqishadi.✅\nMurojaat uchun: +998 77 077 62 36", reply_markup=direction_btn)
            await message.bot.send_message(admin_dilbek, text=f"Yangi ro'yxatdan o'tish:\n\nIsm: <b>{first_name}</b>\nFamiliya: <b>{last_name}</b>\nTelefon: <b>{phone}</b>\nManzil: <b>{address}</b>\nKurs: <b>{course}</b>\nDaraja: <b>{degree}</b>\n\n📅{date}")
            
        elif course == "Matematika":
            await message.bot.send_message(admin_id, text=f"Yangi ro'yxatdan o'tish:\n\nIsm: <b>{first_name}</b>\nFamiliya: <b>{last_name}</b>\nTelefon: <b>{phone}</b>\nManzil: <b>{address}</b>\nKurs: <b>{course}</b>\n\n📅{date}")
            await message.bot.send_message(message.from_user.id, "Adminlar siz bilan aloqaga chiqishadi.✅\nMurojaat uchun: +998 77 077 62 36", reply_markup=direction_btn)
            await message.bot.send_message(admin_dilbek, text=f"Yangi ro'yxatdan o'tish:\n\nIsm: <b>{first_name}</b>\nFamiliya: <b>{last_name}</b>\nTelefon: <b>{phone}</b>\nManzil: <b>{address}</b>\nKurs: <b>{course}</b>\n\n📅{date}")
        else:
            await message.bot.send_message(admin_id, text=f"Yangi ro'yxatdan o'tish:\n\nIsm: <b>{first_name}</b>\nFamiliya: <b>{last_name}</b>\nTelefon: <b>{phone}</b>\nManzil: <b>{address}</b>\nKurs: <b>{course}</b>\n\n📅{date}")
            await message.bot.send_message(message.from_user.id, "Adminlar siz bilan aloqaga chiqishadi.✅\nMurojaat uchun: +998 50 506 22 11", reply_markup=direction_btn)

        await state.clear()