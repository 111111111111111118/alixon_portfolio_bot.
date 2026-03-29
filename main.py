import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# 1. BOT TOKEN
TOKEN = "8787110745:AAFd7HzZ8YucGRvLhETCnw8a9Lvew2knbGU"

dp = Dispatcher()

# GitHub manzili (Sertifikatlarim/ papkasi olib tashlandi, chunki fayllar ochiq turibdi)
BASE_URL = "https://raw.githubusercontent.com/11111111111111118/alixon_portfolio_bot/main"

# --- MENYULAR ---

def main_menu():
    buttons = [
        [InlineKeyboardButton(text="🤖 AI va Kiberxavfsizlik", callback_data="cat_ai")],
        [InlineKeyboardButton(text="💻 Dasturlash va IT", callback_data="cat_it")],
        [InlineKeyboardButton(text="🌍 Coursera (Xalqaro)", callback_data="cat_coursera")],
        [InlineKeyboardButton(text="🏆 Yutuqlar va G'olibliklar", callback_data="cat_win")],
        [InlineKeyboardButton(text="👨‍💻 Muallif haqida", callback_data="about")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def cert_menu(category):
    buttons = []
    if category == "ai":
        buttons = [
            [InlineKeyboardButton(text="🧠 Amaliy Sun'iy intellekt", url=f"{BASE_URL}/Amaliy%20Sun'iyintellekt.pdf")],
            [InlineKeyboardButton(text="🛡 Kiberxavfsizlik asoslari", url=f"{BASE_URL}/80%20KIBERXAVFSIZLIK%20ASOSLARI.pdf")],
            [InlineKeyboardButton(text="🤖 AI Prompters", url=f"{BASE_URL}/Five%20Million%20AI%20Prompters.pdf")],
            [InlineKeyboardButton(text="📈 GPTni noldan o'rganish", url=f"{BASE_URL}/GPTni%20noldan%20o%E2%80%98rganish.pdf")]
        ]
    elif category == "it":
        buttons = [
            [InlineKeyboardButton(text="🐍 Django asoslari", url=f"{BASE_URL}/Qosimov%20Alixon--.pdf")],
            [InlineKeyboardButton(text="🌐 Frontend", url=f"{BASE_URL}/Frontend.pdf")],
            [InlineKeyboardButton(text="💾 Ma'lumotlar bazasi", url=f"{BASE_URL}/MA'LUMOTLAR%20BAZASI.pdf")],
            [InlineKeyboardButton(text="🎮 Unity Junior Programmer", url=f"{BASE_URL}/Unity%20Junior%20Programmer.pdf")],
            [InlineKeyboardButton(text="🎨 Web Design", url=f"{BASE_URL}/WEB%20DIZAYN.pdf")]
        ]
    elif category == "coursera":
        buttons = [
            [InlineKeyboardButton(text="🎓 Responsive Design", url=f"{BASE_URL}/Coursera%20Advanced%20Styling%20with%20Responsive%20Design.pdf")],
            [InlineKeyboardButton(text="⚙️ Robotatexnika", url=f"{BASE_URL}/Coursera%20Robotatexnika.pdf")],
            [InlineKeyboardButton(text="📜 HTML5 Introduction", url=f"{BASE_URL}/Coursera%20Introduction%20to%20HTML5.pdf")]
        ]
    elif category == "win":
        buttons = [
            [InlineKeyboardButton(text="🏆 Eng tezkor texnik (TerDU)", url=f"{BASE_URL}/TerDU%20Eng%20tezkor%20texnik.PDF")],
            [InlineKeyboardButton(text="🌟 Mirzo Ulug'bek vorislari", url=f"{BASE_URL}/Mirzo%20Ulug'bek%20vorislari.jpg")]
        ]
    
    buttons.append([InlineKeyboardButton(text="⬅️ Orqaga", callback_data="back")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)

# --- HANDLERS ---

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(
        f"Assalomu alaykum, {message.from_user.full_name}!\n\n"
        "Qosimov Alixon Alimovichning barcha sertifikatlari jamlangan portfolio botiga xush kelibsiz.\n"
        "Bo'limni tanlang:",
        reply_markup=main_menu()
    )

@dp.callback_query(F.data.startswith("cat_"))
async def show_category(callback: types.CallbackQuery):
    cat = callback.data.split("_")[1]
    await callback.message.edit_text("Sertifikatni tanlang:", reply_markup=cert_menu(cat))

@dp.callback_query(F.data == "back")
async def back_to_main(callback: types.CallbackQuery):
    await callback.message.edit_text("Bo'limni tanlang:", reply_markup=main_menu())

@dp.callback_query(F.data == "about")
async def about(callback: types.CallbackQuery):
    info = (
        "👤 **Muallif:** Qosimov Alixon Alimovich\n"
        "🎓 **O'qish:** Termiz Davlat Universiteti (KI-223 guruh)\n"
        "💻 **Kasbi:** Kompyuter xizmatlari mutaxassisi\n"
        "🛠 **Texnologiyalar:** Django, Python, IoT, Data Recovery"
    )
    await callback.message.answer(info, parse_mode="Markdown")
    await callback.answer()

async def main():
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
