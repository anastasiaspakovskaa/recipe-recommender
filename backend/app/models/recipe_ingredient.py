from sqlalchemy import ForeignKey, String, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..database import Base


class RecipeIngredient(Base):
    __tablename__ = "recipe_ingredients"

    id: Mapped[int] = mapped_column(primary_key=True)

    recipe_id: Mapped[int] = mapped_column(
        ForeignKey("recipes.id"),
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

    recipe: Mapped["Recipe"] = relationship(
        back_populates="recipe_ingredients"
    )

    ingredient: Mapped["Ingredient"] = relationship(
        back_populates="recipe_ingredients"
    )