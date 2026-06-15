import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from app.bot.handlers.my_games import router as my_games_router
from app.bot.handlers.remove import router as remove_router
from app.bot.handlers.search import router as search_router
from app.bot.handlers.track import router as track_router
from app.config import settings
from app.database.session import create_tables
from app.services.price_checker import PriceChecker
from app.services.user_service import UserService

bot = Bot(token=settings.bot_token)
dp = Dispatcher()
scheduler = AsyncIOScheduler()

dp.include_router(search_router)
dp.include_router(track_router)
dp.include_router(my_games_router)
dp.include_router(remove_router)


@dp.message(Command("start"))
async def start_handler(message: Message) -> None:
    await UserService.get_or_create(
        telegram_id=message.from_user.id,
        username=message.from_user.username,
    )
    await message.answer("🎮 Steam Price Alert is running!")


@dp.message(Command("help"))
async def help_handler(message: Message) -> None:
    await message.answer("Available commands: /start /help /search /track /my_games /remove")


async def run_price_checker() -> None:
    checker = PriceChecker()
    notifications = await checker.check_prices()

    for notification in notifications:
        await bot.send_message(
            notification["user_id"],
            (
                f"🔥 Price alert!\n\n"
                f"Game: {notification['game_name']}\n"
                f"Current price: {notification['current_price']} "
                f"{notification['currency']}\n"
                f"Target price: {notification['target_price']}\n"
                f"Shop: {notification['shop']}"
            ),
        )


async def main() -> None:
    await create_tables()

    scheduler.add_job(
        run_price_checker,
        trigger="interval",
        hours=6,
    )
    scheduler.start()

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
