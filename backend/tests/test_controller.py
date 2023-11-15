from src.controller import food
from src.schemas.food import FoodCreate


def test_food_create(session):
    new_food = food.create(
        session,
        FoodCreate(name="Teste", price=100, image="https://google.com.br"),
    )

    created_food = (
        session.query(food.model)
        .where(food.model.name == new_food.name)
        .first()
    )

    assert created_food.name == new_food.name
