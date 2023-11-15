from pydantic import BaseModel, ConfigDict


class FoodBase(BaseModel):
    name: str
    price: float
    image: str


class FoodCreate(FoodBase):
    pass


class FoodInDBBase(FoodBase):
    model_config = ConfigDict(from_attributes=True)

    id: int


class Food(FoodInDBBase):
    pass
