import aiohttp

from app.config import settings


class ITADClient:
    BASE_URL = "https://api.isthereanydeal.com"

    async def search(self, title: str):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{self.BASE_URL}/games/search/v1",
                params={"key": settings.itad_api_key, "title": title},
            ) as response:
                return await response.json()
