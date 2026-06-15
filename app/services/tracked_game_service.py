from sqlalchemy import delete, select

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

    @staticmethod
    async def remove_game(user_id: int, game_id: str) -> None:
        async with async_session() as session:
            await session.execute(
                delete(TrackedGame).where(
                    TrackedGame.user_id == user_id,
                    TrackedGame.game_id == game_id,
                )
            )
            await session.commit()
