from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.services.tracked_game_service import TrackedGameService

router = Router()


@router.message(Command("track"))
async def track_handler(message: Message) -> None:
    parts = message.text.split()

    if len(parts) != 3:
        await message.answer("Usage: /track <itad_uuid> <target_price>")
        return

    game_id = parts[1]

    try:
        target_price = int(parts[2])
    except ValueError:
        await message.answer("Target price must be a number.")
        return

    await TrackedGameService.add_game(
        user_id=message.from_user.id,
        game_id=game_id,
        game_name=game_id,
        target_price=target_price,
    )

    await message.answer("Game added to tracking.")
