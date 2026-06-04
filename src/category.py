class Category():
    """Класс категорий"""
    name: str
    description: str
    products: list

    def __init__(self, name, description, products=None):
        """Инициализауия атрибутов объектов класса категорий"""
        self.name = name,
        self.description = description,
        self.products = products if products else []
