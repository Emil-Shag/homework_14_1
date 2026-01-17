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
        result = cls(
            name=dictionary["name"],
            description=dictionary["description"],
            price=dictionary["price"],
            quantity=dictionary["quantity"],
        )
        return result

    def __str__(self):
        """Отображает информацию о товаре в виде строки."""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Подсчитывает стоимость товаров на складе"""
        if type(self) == type(other):
            return self.__price * self.quantity + other.__price * other.quantity
        raise TypeError


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
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products(self):
        """Геттер для формирования списка товаров"""
        result = []
        for prod in self.__products:
            result.append(f"{prod.name}, {prod.price} руб. Остаток: {prod.quantity} шт.")
        return result

    def __str__(self):
        """Отображает количество продуктов по категориям"""
        result = 0
        for product in self.__products:
            result += product.quantity
        return f"{self.name}, количество продуктов: {result} шт."

class Smartphone(Product):
    """Класс для категории товара: Смартфон"""
    efficiency: float
    model: str
    memory: int
    color: str

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

class LawnGrass(Product):
    """Класс для категории товара: Трава газонная"""
    country: str
    germination_period: str
    color: str

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
