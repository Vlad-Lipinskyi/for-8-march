import asyncio
import random
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram import F

TOKEN = "8587415331:AAHzZpuSQSXL4cT67u-p1pvNxSWo4DbqWK8"

bot = Bot(token=TOKEN)
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)

compliments = [
    "Ти найкраща мама у світі 💖",
    "Ти завжди підтримуєш мене 🌸",
    "Твоя усмішка робить мій день кращим ☀️",
    "Ти моя опора і натхнення 💐",
    "З тобою завжди тепло і спокійно 🫶"
]

thanks = [
    "Дякую тобі за турботу 💖",
    "Дякую за смачну їжу 🍲",
    "Дякую за терпіння і любов 🌷",
    "Дякую, що завжди віриш у мене 🌟"
]

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🌷 Комплімент")],
        [KeyboardButton(text="💖 Подяка")]
    ],
    resize_keyboard=True
)

@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer(
        "Привіт, мама 💐\nЦей бот створений спеціально для тебе ❤️\nЗ 8 березня 🌷",
        reply_markup=keyboard
    )

@dp.message(F.text == "🌷 Комплімент")
async def send_compliment(message: Message):
    await message.answer(random.choice(compliments))

@dp.message(F.text == "💖 Подяка")
async def send_thanks(message: Message):
    await message.answer(random.choice(thanks))

@dp.message(Command("compliment"))
async def compliment_command(message: Message):
    await message.answer(random.choice(compliments))

@dp.message(Command("thanks"))
async def thanks_command(message: Message):
    await message.answer(random.choice(thanks))

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())