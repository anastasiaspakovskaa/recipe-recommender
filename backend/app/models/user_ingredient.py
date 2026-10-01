from sqlalchemy import Float, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..database import Base


class UserIngredient(Base):
    __tablename__ = "user_ingredients"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    ingredient_id: Mapped[int] = mapped_column(
        ForeignKey("ingredients.id"),
        nullable=False
    )

    quantity: Mapped[float | None] = mapped_column(
        Float, 
        nullable=True
    )

    unit: Mapped[str | None] = mapped_column(
        String(30),
        nullable=True
    )

    user: Mapped["User"] = relationship(
        back_populates="user_ingredients"
    )

    ingredient: Mapped["Ingredient"] = relationship(
        back_populates="user_ingredients"
    )