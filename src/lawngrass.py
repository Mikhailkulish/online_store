from src.product import Product


class LawnGrass(Product):
    """Класс газонокосилок"""

    def __init__(self, name, description, __price, quantity, country, germination_period, color):
        """Инициализация атрибутов объектов класса газонокосилок"""
        super().__init__(name, description, __price, quantity, country, germination_period, color)
        self.country = country
        self.germination_period = germination_period
        self.color = color
