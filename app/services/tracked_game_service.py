from sqlalchemy import select

from app.database.models.tracked_game import TrackedGame
from app.database.session import async_session


class TrackedGameService:
    @staticmethod
    async def add_game(user_id: int, game_id: str, game_name: str, target_price: int) -> TrackedGame:
        async with async_session() as session:
            game = TrackedGame(
                user_id=user_id,
                game_id=game_id,
                game_name=game_name,
                target_price=target_price,
            )
            session.add(game)
            await session.commit()
            await session.refresh(game)
            return game

    @staticmethod
    async def get_user_games(user_id: int) -> list[TrackedGame]:
        async with async_session() as session:
            result = await session.execute(select(TrackedGame).where(TrackedGame.user_id == user_id))
            return list(result.scalars().all())
