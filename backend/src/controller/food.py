from src.database.models import Food
from src.schemas.food import FoodCreate

from ._base import BaseCRUD


class FoodCRUD(BaseCRUD[Food, FoodCreate]):
    pass


food = FoodCRUD(Food)
