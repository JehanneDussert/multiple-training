import requests
from typing import Dict
from pydantic import BaseModel

url = "https://fakestoreapi.com/products/1"

response = requests.get(url)
json_data = response.json()

class Rating(BaseModel):
    rate: float
    count: int

class Fake_Data(BaseModel):
    id: int
    title: str
    price: float
    description: str
    category: str
    image: str
    rating: Rating

data = Fake_Data(**json_data)

print('data: ', data)