import pytest

from src.classes import Category, LawnGrass, Product, Smartphone


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

    with pytest.raises(ValueError):
        product_example_1.price = -1000000


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
    category_example._add_product(product_example_3)

    assert len(category_example.products) == 3
    assert "Xiaomi 228 Turbo XXL" in category_example.products[2]
    assert Category.product_count == 3


def test_count_products(category_example):
    assert Category.product_count == 2


def test_count_categories(category_example):
    assert Category.category_count == 1


def test_str_product(product_example_1):
    assert str(product_example_1) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_add_method_product(product_example_1, product_example_2):
    assert product_example_1 + product_example_2 == 2580000.0


def test_str_categories(category_example):
    assert str(category_example) == "Смартфоны, количество продуктов: 13 шт."


@pytest.fixture
def smartphone_example_1():
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


def test_smartphone_init(smartphone_example_1):
    assert smartphone_example_1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone_example_1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone_example_1.price == 180000.0
    assert smartphone_example_1.quantity == 5
    assert smartphone_example_1.efficiency == 95.5
    assert smartphone_example_1.model == "S23 Ultra"
    assert smartphone_example_1.memory == 256
    assert smartphone_example_1.color == "Серый"


@pytest.fixture
def lawn_grass_example_1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


def test_lawn_grass_init(lawn_grass_example_1):
    assert lawn_grass_example_1.name == "Газонная трава"
    assert lawn_grass_example_1.description == "Элитная трава для газона"
    assert lawn_grass_example_1.price == 500.0
    assert lawn_grass_example_1.quantity == 20
    assert lawn_grass_example_1.country == "Россия"
    assert lawn_grass_example_1.germination_period == "7 дней"
    assert lawn_grass_example_1.color == "Зеленый"


def test_invalid_add_method_product(smartphone_example_1, lawn_grass_example_1):
    with pytest.raises(TypeError):
        smartphone_example_1 + lawn_grass_example_1


def test_invalid_add_product(category_example, capsys):
    category_example.safe_add("invalid_product_example")
    captured = capsys.readouterr()
    assert "Ошибка: Товар должен быть в Product\nОбработка добавления товара завершена\n" in captured.out



def test_mixin(capsys):
    Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    message = capsys.readouterr()
    assert message.out.strip() == "Product(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)"

def test_init_invalid_product():
    with pytest.raises(ValueError):
        Product("Бракованный товар", "Неверное количество", 1000.0, 0)

@pytest.fixture
def category_empty_example():
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [],
    )

def test_count_zero_middle_price(category_empty_example):
    assert category_empty_example.middle_price() == 0