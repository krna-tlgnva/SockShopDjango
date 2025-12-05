import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

TOKEN = "7820350921:AAGPHSIxBBjICYy5SCIbN-IHhFOlrmX-zQk"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command('start'))
async def start(message: types.Message):
    await message.answer("Bot works")

async def main():
    await dp.start_polling(bot, skip_updates=True)

if __name__ == "__main__":
    asyncio.run(main())