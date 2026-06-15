from app.services.itad_client import ITADClient
from app.services.tracked_game_service import TrackedGameService


class PriceChecker:
    def __init__(self) -> None:
        self.itad_client = ITADClient()

    async def check_prices(self) -> list[dict]:
        notifications = []

        games = await TrackedGameService.get_all_games()

        for game in games:
            price_data = await self.itad_client.get_price(game.game_id)

            if price_data is None:
                continue

            current_price = price_data["price"]

            if current_price <= game.target_price:
                notifications.append(
                    {
                        "user_id": game.user_id,
                        "game_name": game.game_name,
                        "current_price": current_price,
                        "target_price": game.target_price,
                        "currency": price_data["currency"],
                        "shop": price_data["shop"],
                    }
                )

        return notifications
