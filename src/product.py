class Product():
    """Класс продуктов"""
    name: str
    description: str
    price: float
    quanity: int

    def __init__(self, name, description, price, quanity):
        """Инициализауия атрибутов объектов класса продуктов"""
        self.name = name,
        self.description = description,
        self.price = price,
        self.quanity = quanity
