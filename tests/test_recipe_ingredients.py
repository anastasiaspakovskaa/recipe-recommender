def test_add_ingredient_to_recipe(client):
    ingredient_response = client.post(
        "/ingredients",
        json={"name": "Flour"},
    )
    assert ingredient_response.status_code == 201
    ingredient_id = ingredient_response.json()["id"]

    recipe_response = client.post(
        "/recipes",
        json={
            "name": "Pancakes",
            "description": "Simple pancakes",
            "instructions": "Mix and fry.",
            "calories": 300,
        },
    )
    assert recipe_response.status_code == 201
    recipe_id = recipe_response.json()["id"]

    response = client.post(
        f"/recipes/{recipe_id}/ingredients",
        json={
            "ingredient_id": ingredient_id,
            "quantity": 200,
            "unit": "g",
        },
    )

    assert response.status_code == 201
    assert response.json()["recipe_id"] == recipe_id
    assert response.json()["ingredient_id"] == ingredient_id
    assert response.json()["quantity"] == 200
    assert response.json()["unit"] == "g"