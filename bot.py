from aiogram import Bot, Dispatcher, types, Router, F
from aiogram.filters import CommandStart, Command
from config import API_TOKEN
import asyncio

bot = Bot(token=API_TOKEN)
dp = Dispatcher()
router = Router()

@router.message(CommandStart())
async def start(message: types.Message):
    await message.answer("Привет! Я echo bot. Напиши мне что-нибудь, и я повторю.")

@router.message(Command("help"))
async def help_cmd(message: types.Message):
    help_text = "Доступные команды:\n/start - начать общение\n/help - помощь"
    await message.answer(help_text)

@router.message(F.text)
async def echo(message: types.Message):
    await message.answer(f"Вы сказали: {message.text}")

async def main():
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())