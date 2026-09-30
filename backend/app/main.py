from fastapi import FastAPI
from sqlalchemy import text

from .database import Base, engine
from .models.user import User
from .models.ingredient import Ingredient
from .models.recipe import Recipe
from .models.recipe_ingredient import RecipeIngredient
from .models.user_ingredient import UserIngredient

app = FastAPI(title="Recipe Recommendation API")


Base.metadata.create_all(bind=engine)


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/health/db")
def database_health_check():
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))

    return {"status": "ok", "database": "connected"}