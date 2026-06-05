class Product:
    """Класс продуктов"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Инициализауия атрибутов объектов класса продуктов"""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
