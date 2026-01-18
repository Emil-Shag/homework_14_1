import json
import pytest
from unittest.mock import mock_open, patch

from src.json_reader import json_reader, create_objects_from_json


def test_open_file():

    mock_data = [{"some": 1, "mocked": 2},{"data": 3}]

    mock_json = json.dumps(mock_data)

    m = mock_open(read_data=mock_json)

    with patch("builtins.open", m):
        with patch("os.path.abspath", return_value="fake/path.json"):
            result = json_reader("some/path.json")

    assert result == mock_data

@pytest.mark.parametrize("input_data, expected_categories_count, expected_products_count", [([
  {
    "name": "Смартфоны",
    "products": [
      {
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
      },
      {
        "name": "Iphone 15",
        "description": "512GB, Gray space",
        "price": 210000.0,
        "quantity": 8
      },
      {
        "name": "Xiaomi Redmi Note 11",
        "description": "1024GB, Синий",
        "price": 31000.0,
        "quantity": 14
      }
    ]
  },
  {
    "name": "Телевизоры",
    "products": [
      {
        "name": "55\" QLED 4K",
        "description": "Фоновая подсветка",
        "price": 123000.0,
        "quantity": 7
      }
    ]
  }
], 2, 4), ([],0,0,),],)

def test_create_objects_from_json(input_data, expected_categories_count, expected_products_count):
    with patch("src.json_reader.Product") as MockProduct, patch("src.json_reader.Category") as MockCategory:
        result = create_objects_from_json(input_data)


    assert len(result) == expected_categories_count
    assert MockCategory.call_count == expected_categories_count
    assert MockProduct.call_count == expected_products_count