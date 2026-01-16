import pytest

from src.classes import Category, Product


@pytest.fixture(autouse=True)
def reset_category_counters():
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def product_example_1():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def product_example_2():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def category_example(product_example_1, product_example_2):
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product_example_1, product_example_2],
    )


def test_init_product(product_example_1):
    assert product_example_1.name == "Samsung Galaxy S23 Ultra"
    assert product_example_1.description == "256GB, Серый цвет, 200MP камера"
    assert product_example_1.price == 180000.0
    assert product_example_1.quantity == 5


def test_product_price_setter(product_example_1):
    product_example_1.price = 1000000
    assert product_example_1.price == 1000000

    product_example_1.price = -1000000
    assert product_example_1.price == 1000000


def test_new_product():
    dictionary = {
        "name": "Xiaomi 228 Turbo XXL",
        "description": "7000 GB, Розовый цвет, 17000 MP камера",
        "price": 15000,
        "quantity": 9999,
    }
    result = Product.new_product(dictionary)

    assert result.name == "Xiaomi 228 Turbo XXL"
    assert result.description == "7000 GB, Розовый цвет, 17000 MP камера"
    assert result.price == 15000
    assert result.quantity == 9999


def test_init_category(category_example):
    assert category_example.name == "Смартфоны"
    assert (
        category_example.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert "Samsung Galaxy S23 Ultra" in category_example.products[0]
    assert "Iphone 15" in category_example.products[1]


def test_add_product(category_example):
    product_example_3 = Product("Xiaomi 228 Turbo XXL", "7000 GB, Розовый цвет, 17000 MP камера", 15000, 9999)
    category_example.add_product(product_example_3)

    assert len(category_example.products) == 3
    assert "Xiaomi 228 Turbo XXL" in category_example.products[2]
    assert Category.product_count == 3


def test_count_products(category_example):
    assert Category.product_count == 2


def test_count_categories(category_example):
    assert Category.category_count == 1
