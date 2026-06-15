import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

from app.config import settings
from app.services.user_service import UserService

bot = Bot(token=settings.bot_token)
dp = Dispatcher()


@dp.message(Command("start"))
async def start_handler(message: Message) -> None:
    await UserService.get_or_create(
        telegram_id=message.from_user.id,
        username=message.from_user.username,
    )
    await message.answer("🎮 Steam Price Alert is running!")


@dp.message(Command("help"))
async def help_handler(message: Message) -> None:
    await message.answer("Available commands: /start /help")


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
