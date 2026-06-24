from src.product import Product


class Smartphone(Product):
    """Класс смартфонов"""

    def __init__(self, name, description, __price, quantity, efficiency, model, memory, color):
        """Инициализация атрибутов объектов класса смартфонов"""
        super().__init__(name, description, __price, quantity, efficiency, model, memory, color)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
