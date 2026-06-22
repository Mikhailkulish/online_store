from src.category import Category


class Smartphone(Category):
    """Класс смартфонов"""

    name: str
    description: str
    products: list

    def __init__(self, name, description, products, efficiency, model, memory, color):
        """Инициализация атрибутов объектов класса смартфонов"""
        super().__init__(name, description, products)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
