from src.category import Category


class LawnGrass(Category):
    """Класс газонокосилок"""

    name: str
    description: str
    products: list

    def __init__(self, name, description, products, country, germination_period, color):
        """Инициализация атрибутов объектов класса газонокосилок"""
        super().__init__(name, description, products)
        self.country = country
        self.germination_period = germination_period
        self.color = color
