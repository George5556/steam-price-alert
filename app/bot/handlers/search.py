from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.services.itad_client import ITADClient

router = Router()
client = ITADClient()


@router.message(Command("search"))
async def search_handler(message: Message) -> None:
    query = message.text.replace("/search", "", 1).strip()

    if not query:
        await message.answer("Usage: /search <game name>")
        return

    results = await client.search(query)

    if not results:
        await message.answer("No games found.")
        return

    lines = []

    for game in results[:5]:
        lines.append(f"{game['title']}\nUUID: {game['id']}")

    await message.answer("\n\n".join(lines))
