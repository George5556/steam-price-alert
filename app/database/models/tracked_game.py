from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.models.base import Base


class TrackedGame(Base):
    __tablename__ = "tracked_games"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    game_id: Mapped[str] = mapped_column(String(100))
    game_name: Mapped[str] = mapped_column(String(255))
    target_price: Mapped[int] = mapped_column(Integer)
