from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime


class RecipeCreate(BaseModel):
    name: str = Field(min_length=1, max_length=200)
    description: str | None = None
    instructions: str = Field(min_length=1)
    calories: int | None = Field(default=None, ge=0)


class RecipeResponse(BaseModel):
    id: int
    name: str
    description: str | None
    instructions: str
    calories: int | None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)