from abc import ABC, abstractmethod


class BaseClass(ABC):
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def safe_add(self, product):
        """Метод для добавления в список товаров объект Product"""
        try:
            if not isinstance(product, Product):
                raise TypeError("Товар должен быть в Product")
            if product.quantity == 0:
                raise ZeroQuantityError("Товар с нулевым количеством не добавлен")

        except (ZeroQuantityError, TypeError) as e:
            print(f"Ошибка: {e}")

        else:
            self._add_product(product)
            print(f"Товар '{product.name}' добавлен")

        finally:
            print("Обработка добавления товара завершена")

    @abstractmethod
    def _add_product(self, product: "Product"):

        pass


class ZeroQuantityError(Exception):
    """Класс исключения, исключающий добавление товара с нулевым количеством"""

    def __init__(self, message="Товар с нулевым количеством не добавлен."):
        super().__init__(message)


class BaseProduct(ABC):
    """Абстрактный класс для продуктов"""

    name: str
    description: str
    price: float
    quantity: int

    @abstractmethod
    def __init__(self, *args, **kwargs):
        """Абстрактный инициализатор"""
        pass

    @property
    @abstractmethod
    def price(self):
        pass

    @price.setter
    @abstractmethod
    def price(self, value):
        pass

    def __add__(self, other):
        """Подсчитывает стоимость товаров на складе"""
        if type(self) == type(other):
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError

    def __str__(self):
        """Отображает информацию о товаре в виде строки."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."


class MixinPrint:
    def __init__(self):
        print(repr(self))

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"


class Product(MixinPrint, BaseProduct):
    """Класс для представления продуктов"""

    def __init__(self, name, description, price, quantity):
        """Метод для инициализации экземпляра класса"""

        self.name = name
        self.description = description
        self.__price = price
        if quantity > 0:
            self.quantity = quantity
        else:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        super().__init__()

    @classmethod
    def new_product(cls, dictionary, product_list=None):
        if product_list:
            for prod in product_list:
                if prod.name == dictionary["name"]:
                    prod.quantity += dictionary["quantity"]
                    prod.price = max(dictionary["price"], prod.price)
                    return prod

        return cls(
            name=dictionary["name"],
            description=dictionary["description"],
            price=dictionary["price"],
            quantity=dictionary["quantity"],
        )

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Цена должна быть положительной")

        if value > self.__price:
            self.__price = value
        elif value < self.__price:
            user_input = input("Понизить цену? y/n: ").lower()
            if user_input == "y":
                self.__price = value
            else:
                print("Цена не изменена")


class Category(BaseClass):
    """Класс для представления категорий"""

    name: str
    description: str
    products: list

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        """Метод для инициализации экземпляра класса"""
        super().__init__(name, description)
        self.__products = []

        Category.category_count += 1
        if products:
            for product in products:
                self._add_product(product)

    def _add_product(self, product):
        self.__products.append(product)
        Category.product_count += 1

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

    def middle_price(self):
        """Подсчитывает средний ценник всех товаров"""
        try:
            return sum([products.price for products in self.__products]) / len(self.__products)
        except ZeroDivisionError:
            return 0


class Smartphone(Product):
    """Класс для категории товара: Смартфон"""

    efficiency: float
    model: str
    memory: int
    color: str

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        """Метод для инициализации экземпляра класса: Смартфон"""
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
        """Метод для инициализации экземпляра класса: Трава газонная"""
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


class IterProducts:
    """Итератор, перебирающий товары одной категории"""

    def __init__(self, category: Category):
        self.__products = category.products
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.__products):
            product = self.__products[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration


class Order(BaseClass):
    def __init__(self, product, quantity):
        super().__init__(name=product.name, description=product.description)
        self.product = product
        self.quantity = quantity
        self.final_price = self.calculate_price()

    def calculate_price(self):
        return self.product.price * self.quantity

    def _add_product(self, product):
        self.product = product
        self.quantity = product.quantity
        self.final_price = self.calculate_price()
