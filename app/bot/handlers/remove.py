from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.services.tracked_game_service import TrackedGameService

router = Router()


@router.message(Command("remove"))
async def remove_handler(message: Message) -> None:
    parts = message.text.split()

    if len(parts) != 2:
        await message.answer("Usage: /remove <game_id>")
        return

    await TrackedGameService.remove_game(
        user_id=message.from_user.id,
        game_id=parts[1],
    )

    await message.answer("Game removed from tracking.")
