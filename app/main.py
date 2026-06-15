import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

from app.bot.handlers.my_games import router as my_games_router
from app.bot.handlers.search import router as search_router
from app.bot.handlers.track import router as track_router
from app.config import settings
from app.services.user_service import UserService

bot = Bot(token=settings.bot_token)
dp = Dispatcher()
dp.include_router(search_router)
dp.include_router(track_router)
dp.include_router(my_games_router)


@dp.message(Command("start"))
async def start_handler(message: Message) -> None:
    await UserService.get_or_create(
        telegram_id=message.from_user.id,
        username=message.from_user.username,
    )
    await message.answer("🎮 Steam Price Alert is running!")


@dp.message(Command("help"))
async def help_handler(message: Message) -> None:
    await message.answer("Available commands: /start /help /search /track /my_games")


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
