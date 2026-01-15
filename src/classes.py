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
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value > 0:
            self.__price = value
        else:
            print("Цена не должна быть нулевая или отрицательная")

    @classmethod
    def new_product(cls, dictionary):
        result = cls(name=dictionary['name'],
            description=dictionary['description'],
            price=dictionary['price'],
            quantity=dictionary['quantity'])
        return result

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
        if products:
            for product in products:
                self.add_product(product)

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

