import aiohttp

from app.config import settings


class ITADClient:
    BASE_URL = "https://api.isthereanydeal.com"
