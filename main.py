import asyncio
import logging
import sys
from urllib.parse import quote
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

# 1. BOT TOKEN
TOKEN = "8787110745:AAFd7HzZ8YucGRvLhETCnw8a9Lvew2knbGU"

dp = Dispatcher()

# GitHub manzilingiz (Fayllar turgan joy)
BASE_URL = "https://raw.githubusercontent.com/11111111111111118/alixon_portfolio_bot/main"

def get_url(filename):
    """Fayl nomlarini URL uchun xavfsiz formatga o'tkazish"""
    return f"{BASE_URL}/{quote(filename)}"

# --- MENYULAR ---

def main_menu():
    buttons = [
        [InlineKeyboardButton(text="🤖 Sun'iy Intellekt va Robototexnika", callback_data="cat_ai")],
        [InlineKeyboardButton(text="💻 Dasturlash (Django & Frontend)", callback_data="cat_it")],
        [InlineKeyboardButton(text="🌍 Coursera (Xalqaro kurslar)", callback_data="cat_coursera")],
        [InlineKeyboardButton(text="📈 Marketing va PM", callback_data="cat_biz")],
        [InlineKeyboardButton(text="🛡 Xavfsizlik va Maxsus yutuqlar", callback_data="cat_sec")],
        [InlineKeyboardButton(text="👨‍💻 Muallif haqida", callback_data="about")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def cert_menu(category):
    buttons = []
    
    if category == "ai":
        buttons = [
            [InlineKeyboardButton(text="🤖 Robotatexnika (Siemens)", url=get_url("Coursera Robotatexnika.pdf"))],
            [InlineKeyboardButton(text="🧠 Amaliy Sun'iy intellekt", url=get_url("Amaliy Sun'iyintellekt.pdf"))],
            [InlineKeyboardButton(text="✨ SI foydalanish", url=get_url("Sun’iy intellektlardan foydalanish.pdf"))],
            [InlineKeyboardButton(text="📊 SI salohiyatini baholash", url=get_url("Sun’iyintellekt texnologiyalaridan foydalanish bo‘yicha.pdf"))],
            [InlineKeyboardButton(text="🤖 AI Prompters", url=get_url("Five Million AI Prompters.pdf"))],
            [InlineKeyboardButton(text="📈 GPTni noldan o'rganish", url=get_url("GPTni noldan o‘rganish.pdf"))]
        ]
    elif category == "it":
        buttons = [
            [InlineKeyboardButton(text="🎯 Django asoslari", url=get_url("Qosimov Alixon--.pdf"))],
            [InlineKeyboardButton(text="🌐 Frontend Dasturlash", url=get_url("Frontend.pdf"))],
            [InlineKeyboardButton(text="💾 Ma'lumotlar bazasi", url=get_url("MA'LUMOTLAR BAZASI.pdf"))],
            [InlineKeyboardButton(text="🖥 Kompyuter asoslari", url=get_url("Kompyuter  asoslari.pdf"))],
            [InlineKeyboardButton(text="📋 Umumiy informatika", url=get_url("Umumiy   informatika.pdf"))],
            [InlineKeyboardButton(text="🎮 Unity Programmer", url=get_url("Unity  Junior Programmer.pdf"))],
            [InlineKeyboardButton(text="🎨 Web Design", url=get_url("WEB DESIGN.pdf"))],
            [InlineKeyboardButton(text="🖌 Grafik dizayn", url=get_url("Grafik dizayn.pdf"))]
        ]
    elif category == "coursera":
        buttons = [
            [InlineKeyboardButton(text="📄 Intro to HTML5", url=get_url("Coursera Introduction to HTML5.pdf"))],
            [InlineKeyboardButton(text="📜 Intro to CSS3", url=get_url("Coursera Introduction to CSS3.pdf"))],
            [InlineKeyboardButton(text="⚡ Interactivity with JS", url=get_url("Coursera Interactivity with JavaScript.pdf"))],
            [InlineKeyboardButton(text="📱 Responsive Design", url=get_url("Coursera Advanced Styling with Responsive Design.pdf"))],
            [InlineKeyboardButton(text="🖌 Web Design Capstone", url=get_url("Coursera Web Design for Everybody Capstone.pdf"))],
            [InlineKeyboardButton(text="🐳 Docker & Kubernetes", url=get_url("Coursera Docker, Kubernetes.pdf"))],
            [InlineKeyboardButton(text="🎓 Laravel & PHP Master", url=get_url("Coursera 0HBOUT3EYM5Y.pdf"))],
            [InlineKeyboardButton(text="🎖 Coursera Specialization", url=get_url("Coursera 5.pdf"))]
        ]
    elif category == "biz":
        buttons = [
            [InlineKeyboardButton(text="📅 PM Intro (IBM)", url=get_url("Coursera Introduction to Project Management.pdf"))],
            [InlineKeyboardButton(text="🏗 PM Foundations", url=get_url("Coursera Project Management Foundations, Initiation, and.pdf"))],
            [InlineKeyboardButton(text="⚙️ AT-Loyihalarni boshqarish", url=get_url("AT-LOYIHALARNI BOSHQARISH.pdf"))],
            [InlineKeyboardButton(text="🛒 Elektron tijorat", url=get_url("ELEKTRON TIJORAT.pdf"))],
            [InlineKeyboardButton(text="🎥 SMM video-kurs", url=get_url("SMM - Social Media Marketing video-o'quv kursi.pdf"))],
            [InlineKeyboardButton(text="📱 SMM qo'llanma", url=get_url("IJTIMOIY MEDIA MARKETING o'quv qo'llanma.pdf"))]
        ]
    elif category == "sec":
        buttons = [
            [InlineKeyboardButton(text="🎖 Mirzo Ulug'bek vorislari", url=get_url("Mirzo Ulug'bek vorislari.jpg"))],
            [InlineKeyboardButton(text="⚡ Eng tezkor texnik (TerDU)", url=get_url("TerDU Eng tezkor texnik.PDF"))],
            [InlineKeyboardButton(text="🛡 Cybersecurity Essentials", url=get_url("Coursera Introduction to Cybersecurity Essentials.pdf"))],
            [InlineKeyboardButton(text="🛡 Cyber Case Studies", url=get_url("Coursera Cybersecurity Case Studies and Capstone Project.pdf"))],
            [InlineKeyboardButton(text="🛡 Kiberxavfsizlik asoslari", url=get_url("80  KIBERXAVFSIZLIK ASOSLARI.pdf"))],
            [InlineKeyboardButton(text="💰 Moliyaviy xavfsizlik", url=get_url("Moliyaviyxavfsizlik.pdf"))],
            [InlineKeyboardButton(text="🏛 my.gov.uz xizmatlari", url=get_url("my.gov.uz.pdf"))]
        ]
    
    buttons.append([InlineKeyboardButton(text="⬅️ Orqaga", callback_data="back")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)

# --- HANDLERS ---

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(
        f"Assalomu alaykum, <b>{message.from_user.full_name}</b>!\n\n"
        "Qosimov Alixon Alimovichning 40 ta xalqaro va milliy sertifikatlari jamlangan portfolio botiga xush kelibsiz.\n\n"
        "Kerakli bo'limni tanlang:",
        reply_markup=main_menu()
    )

@dp.callback_query(F.data.startswith("cat_"))
async def show_category(callback: types.CallbackQuery):
    cat = callback.data.split("_")[1]
    await callback.message.edit_text("Sertifikatni tanlang:", reply_markup=cert_menu(cat))
    await callback.answer()

@dp.callback_query(F.data == "back")
async def back_to_main(callback: types.CallbackQuery):
    await callback.message.edit_text("Bo'limni tanlang:", reply_markup=main_menu())
    await callback.answer()

@dp.callback_query(F.data == "about")
async def about(callback: types.CallbackQuery):
    info = (
        "👤 <b>Muallif:</b> Qosimov Alixon Alimovich\n"
        "🎓 <b>O'qish:</b> Termiz Davlat Universiteti (KI 223)\n"
        "💻 <b>Mutaxassisligi:</b> Backend Web Developer (Django)\n"
        "🏆 <b>Yutuqlari:</b> 40 dan ortiq sertifikatlar sohibi."
    )
    back_btn = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="⬅️ Orqaga", callback_data="back")]])
    await callback.message.edit_text(info, reply_markup=back_btn)
    await callback.answer()

async def main():
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot to'xtatildi")
