from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.services.tracked_game_service import TrackedGameService

router = Router()


@router.message(Command("track"))
async def track_handler(message: Message) -> None:
    await message.answer("Usage: /track <game_id> <target_price>")
