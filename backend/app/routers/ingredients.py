from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from ..database import get_db
from ..models.ingredient import Ingredient
from ..schemas.ingredient import (
    IngredientCreate,
    IngredientResponse,
)


router = APIRouter(
    prefix="/ingredients",
    tags=["ingredients"],
)


@router.post(
    "",
    response_model=IngredientResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_ingredient(
    ingredient_data: IngredientCreate,
    db: Session = Depends(get_db),
):
    existing_ingredient = db.scalar(
        select(Ingredient).where(
            Ingredient.name == ingredient_data.name
        )
    )

    if existing_ingredient:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Ingredient already exists",
        )

    ingredient = Ingredient(
        name=ingredient_data.name
    )

    db.add(ingredient)
    db.commit()
    db.refresh(ingredient)

    return ingredient


@router.get(
    "",
    response_model=list[IngredientResponse],
)
def get_ingredients(
    db: Session = Depends(get_db),
):
    return db.scalars(
        select(Ingredient).order_by(Ingredient.name)
    ).all()


@router.get(
    "/{ingredient_id}",
    response_model=IngredientResponse,
)
def get_ingredient(
    ingredient_id: int,
    db: Session = Depends(get_db),
):
    ingredient = db.get(Ingredient, ingredient_id)

    if ingredient is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Ingredient not found",
        )

    return ingredient


@router.put(
    "/{ingredient_id}",
    response_model=IngredientResponse,
)
def update_ingredient(
    ingredient_id: int,
    ingredient_data: IngredientCreate,
    db: Session = Depends(get_db),
):
    ingredient = db.get(Ingredient, ingredient_id)

    if ingredient is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Ingredient not found",
        )

    existing_ingredient = db.scalar(
            select(Ingredient).where(
                Ingredient.name == ingredient_data.name,
                Ingredient.id != ingredient_id
            )
        )
    
    if existing_ingredient:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Ingredient already exists",
        )

    ingredient.name = ingredient_data.name

    db.commit()
    db.refresh(ingredient)

    return ingredient


@router.delete(
    "/{ingredient_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_ingredient(
    ingredient_id: int,
    db: Session = Depends(get_db),
):
    ingredient = db.get(Ingredient, ingredient_id)

    if ingredient is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Ingredient not found",
        )
    
    db.delete(ingredient)
    db.commit()