from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.services.tracked_game_service import TrackedGameService

router = Router()


@router.message(Command("my_games"))
async def my_games_handler(message: Message) -> None:
    games = await TrackedGameService.get_user_games(message.from_user.id)

    if not games:
        await message.answer("You are not tracking any games.")
        return

    text = "\n".join(f"{game.game_name} - {game.target_price}" for game in games)
    await message.answer(text)
