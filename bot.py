import asyncio
import random
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

TOKEN = "8587415331:AAHzZpuSQSXL4cT67u-p1pvNxSWo4DbqWK8"

logging.basicConfig(
    level=logging.INFO,
    filename="bot.log",
    encoding="utf-8",
    format="%(asctime)s - %(levelname)s - %(message)s"
)

bot = Bot(token=TOKEN)
dp = Dispatcher()

def log_user_action(message: Message, action: str):
    user = message.from_user

    if user.username:
        user_info = f"@{user.username} ({user.full_name}) {user.id}"
    else:
        user_info = f"{user.full_name} {user.id}"

    logging.info(f"{user_info} -> {action}")

compliments = [
    "Ти найкраща мама у світі 💖",
    "Ти завжди підтримуєш мене 🌸",
    "З тобою завжди тепло і спокійно 🫶"
]

thanks = [
    "Дякую тобі за турботу 💖",
    "Дякую за смачну їжу 🍲",
    "Дякую за любов 🌷",
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
    log_user_action(message, "/start")

    await message.answer(
        "Привіт, мама 💐\nЦей бот створений спеціально для тебе ❤️\nЗ 8 березня 🌷",
        reply_markup=keyboard
    )

@dp.message(F.text == "🌷 Комплімент")
async def send_compliment(message: Message):
    log_user_action(message, "compliment button")
    await message.answer(random.choice(compliments))

@dp.message(F.text == "💖 Подяка")
async def send_thanks(message: Message):
    log_user_action(message, "thanks button")
    await message.answer(random.choice(thanks))

@dp.message(Command("compliment"))
async def compliment_command(message: Message):
    log_user_action(message, "/compliment")
    await message.answer(random.choice(compliments))

@dp.message(Command("thanks"))
async def thanks_command(message: Message):
    log_user_action(message, "/thanks")
    await message.answer(random.choice(thanks))


async def main():
    logging.info("BOT STARTED")

    # інколи webhook блокує polling
    await bot.delete_webhook(drop_pending_updates=True)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())