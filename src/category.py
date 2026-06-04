class Category:
    """Класс категорий"""

    name: str
    description: str
    products: list

    total_categories = 0
    total_products = 0

    def __init__(self, name, description, products=None):
        """Инициализация атрибутов объектов класса категорий"""
        self.name = name
        self.description = description
        self.products = products if products else []

        Category.total_categories += 1
        Category.total_products += len(self.products)

    @property
    def category_count(self):
        return Category.total_categories

    @property
    def product_count(self):
        return Category.total_products
