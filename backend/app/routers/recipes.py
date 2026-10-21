from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from ..database import get_db
from ..models.recipe import Recipe
from ..models.ingredient import Ingredient
from ..models.recipe_ingredient import RecipeIngredient
from ..schemas.recipe import (
    RecipeCreate,
    RecipeResponse,
)
from ..schemas.recipe_ingredient import (
    RecipeIngredientCreate,
    RecipeIngredientResponse,
)


router = APIRouter(
    prefix="/recipes",
    tags=["recipes"],
)


@router.post(
    "",
    response_model=RecipeResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_recipe(
    recipe_data: RecipeCreate,
    db: Session = Depends(get_db),
):
    recipe = Recipe(**recipe_data.model_dump())

    db.add(recipe)
    db.commit()
    db.refresh(recipe)

    return recipe


@router.get("", response_model=list[RecipeResponse])
def get_recipes(db: Session = Depends(get_db)):
    return db.scalars(
            select(Recipe).order_by(Recipe.created_at.desc())
        ).all()


@router.get(
    "/{recipe_id}",
    response_model=RecipeResponse,
)
def get_recipe(
    recipe_id: int,
    db: Session = Depends(get_db),
):
    recipe = db.get(Recipe, recipe_id)

    if recipe is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Recipe not found",
        )

    return recipe


@router.put(
    "/{recipe_id}",
    response_model=RecipeResponse,
)
def update_recipe(
    recipe_id: int,
    recipe_data: RecipeCreate,
    db: Session = Depends(get_db),
):
    recipe = db.get(Recipe, recipe_id)

    if recipe is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Recipe not found",
        )

    recipe.name = recipe_data.name
    recipe.description = recipe_data.description
    recipe.instructions = recipe_data.instructions
    recipe.calories = recipe_data.calories

    db.commit()
    db.refresh(recipe)

    return recipe


@router.delete(
    "/{recipe_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_recipe(
    recipe_id: int,
    db: Session = Depends(get_db),
):
    recipe = db.get(Recipe, recipe_id)

    if recipe is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Recipe not found",
        )
    
    db.delete(recipe)
    db.commit()


@router.post(
    "/{recipe_id}/ingredients",
    response_model=RecipeIngredientResponse,
    status_code=status.HTTP_201_CREATED,
)
def add_ingredient_to_recipe(
    recipe_id: int,
    data: RecipeIngredientCreate,
    db: Session = Depends(get_db),
):
    recipe = db.get(Recipe, recipe_id)

    if recipe is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Recipe not found",
        )

    ingredient = db.get(Ingredient, data.ingredient_id)

    if ingredient is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Ingredient not found",
        )

    recipe_ingredient = RecipeIngredient(
        recipe_id=recipe_id,
        ingredient_id=data.ingredient_id,
        quantity=data.quantity,
        unit=data.unit,
    )

    db.add(recipe_ingredient)
    db.commit()
    db.refresh(recipe_ingredient)

    return recipe_ingredient