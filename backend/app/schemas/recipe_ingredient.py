from pydantic import BaseModel, ConfigDict, Field


class RecipeIngredientCreate(BaseModel):
    ingredient_id: int
    quantity: float | None = Field(default=None, gt=0)
    unit: str | None = Field(default=None, max_length=30)


class RecipeIngredientResponse(BaseModel):
    id: int
    recipe_id: int
    ingredient_id: int
    quantity: float | None
    unit: str | None

    model_config = ConfigDict(from_attributes=True)