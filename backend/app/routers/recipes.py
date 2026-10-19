from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from ..database import get_db
from ..models.recipe import Recipe
from ..schemas.recipe import (
    RecipeCreate,
    RecipeResponse,
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