class Category:
    """Класс категорий"""

    name: str
    description: str
    products: list

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        """Инициализация атрибутов объектов класса категорий"""
        self.name = name
        self.description = description
        self.__products = products if products else []

        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product):
        """Метод для добавления товара в категорию"""
        self.__products.append(product)
        Category.product_count += 1  # увеличиваем счетчик товаров

    @property
    def products(self):
        """Геттер, возвращающий список товаров в заданном формате"""
        if not self.__products:
            return []

        result = []
        for product in self.__products:
            product_str = f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            result.append(product_str)

        return result
