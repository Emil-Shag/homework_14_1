import json
import os

from src.classes import Product, Category

def json_reader(path: str) -> list[dict]:
    full_path = os.path.abspath(path)
    with open(full_path, 'r', encoding="UTF-8") as file:
        data = json.load(file)
    return data

def create_objects_from_json(data):
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))
    return categories

if __name__ == "__main__":
    raw_data = json_reader("../data/products.json")
    users_data = create_objects_from_json(raw_data)
    print(users_data)