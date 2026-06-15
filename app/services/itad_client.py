import aiohttp

from app.config import settings


class ITADClient:
    BASE_URL = "https://api.isthereanydeal.com"

    async def search(self, title: str):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{self.BASE_URL}/games/search/v1",
                params={
                    "key": settings.itad_api_key,
                    "title": title,
                },
            ) as response:
                return await response.json()

    async def get_price(self, game_id: str):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{self.BASE_URL}/games/prices/v3",
                params={
                    "key": settings.itad_api_key,
                    "ids": game_id,
                },
            ) as response:
                data = await response.json()

        if not data:
            return None

        game = data[0]

        if not game.get("deals"):
            return None

        deal = game["deals"][0]

        return {
            "price": deal["price"]["amount"],
            "currency": deal["price"]["currency"],
            "shop": deal["shop"]["name"],
        }
