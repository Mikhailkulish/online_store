from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный базовый класс продуктов"""

    @abstractmethod
    def __init__(self, *args, **kwargs):
        """Абстрактный метод инициализации"""
        pass

    @property
    @abstractmethod
    def price(self):
        """Абстрактный геттер для цены"""
        pass

    @price.setter
    @abstractmethod
    def price(self, new_price):
        """Абстрактный сеттер для цены"""
        pass

    @abstractmethod
    def __str__(self):
        """Абстрактный метод строкового представления"""
        pass

    @abstractmethod
    def __add__(self, other):
        """Абстрактный метод сложения"""
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, product_dict, existing_products=None):
        """Абстрактный класс-метод создания продукта"""
        pass
