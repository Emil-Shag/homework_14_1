class Product:
    """Класс для представления продуктов"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Метод для инициализации экземпляра класса"""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Класс для представления категорий"""

    name: str
    description: str
    products: list

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        """Метод для инициализации экземпляра класса"""
        self.name = name
        self.description = description
        self.__products = []

        Category.category_count += 1

    def add_product(self, product: Product):
        """Метод для добавления в список товаров объект Product"""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """Геттер для формирования списка товаров"""
        result = []
        for prod in self.__products:
            result.append(f"Название продукта: {prod.name}, {prod.price} руб. Остаток: {prod.quantity} шт.")
        return result

