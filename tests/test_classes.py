import pytest

from src.classes import Product, Category

@pytest.fixture(autouse=True)
def reset_category_counters():
    Category.category_count = 0
    Category.product_count = 0

@pytest.fixture
def product_example():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

@pytest.fixture
def category_example():
    return Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                         ["product1", "product2", "product3"])

def test_init_product(product_example):
    assert product_example.name == "Samsung Galaxy S23 Ultra"
    assert product_example.description == "256GB, Серый цвет, 200MP камера"
    assert product_example.price == 180000.0
    assert product_example.quantity == 5

def test_init_category(category_example):
    assert category_example.name == "Смартфоны"
    assert category_example.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    assert category_example.products == ["product1", "product2", "product3"]

def test_count_products(category_example):
    assert Category.product_count == 3

def test_count_categories(category_example):
    assert Category.category_count == 1