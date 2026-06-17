class CategoryIterator:
    """Итератор для перебора товаров в категории"""

    def __init__(self, category):
        """Инициализация итератора"""
        self.products = category.get_products()  # Получаем список продуктов
        self.index = 0

    def __iter__(self):
        """Возвращает сам итератор"""
        return self

    def __next__(self):
        """Возвращает следующий товар в категории"""
        if self.index < len(self.products):
            product = self.products[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
