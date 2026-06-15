from sqlalchemy import select

from app.database.models.user import User
from app.database.session import async_session


class UserService:
    @staticmethod
    async def get_or_create(telegram_id: int, username: str | None) -> User:
        async with async_session() as session:
            result = await session.execute(select(User).where(User.telegram_id == telegram_id))
            user = result.scalar_one_or_none()

            if user:
                return user

            user = User(telegram_id=telegram_id, username=username)
            session.add(user)
            await session.commit()
            await session.refresh(user)
            return user
