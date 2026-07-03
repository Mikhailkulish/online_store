from src.product import Product


class LawnGrass(Product):
    """Класс газонной травы"""

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        """Инициализация атрибутов объектов класса газонной травы"""
        super().__init__(name, description, price, quantity, country, germination_period, color)
        self.country = country
        self.germination_period = germination_period
        self.color = color
