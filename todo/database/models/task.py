from sqlalchemy import String, Integer, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from todo.database.models.database import Base


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String, index=True)
    completed: Mapped[bool] = mapped_column(Boolean, default=False)
