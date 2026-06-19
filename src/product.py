class Product:
    """Класс продуктов"""

    name: str
    description: str
    __price: float  # сделали приватным
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Инициализация атрибутов объектов класса продуктов"""
        self.name = name
        self.description = description
        self.__price = price  # приватный атрибут
        self.quantity = quantity

    @property
    def price(self):
        """Геттер для получения цены"""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Сеттер для установки цены с проверкой и подтверждением понижения"""
        # Проверка на отрицательную или нулевую цену
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        # Проверка: понижается ли цена
        if new_price < self.__price:
            # Запрашиваем подтверждение у пользователя
            user_input = input(f"Цена понижается с {self.__price} до {new_price}. Вы согласны? (y/n): ")
            if user_input.lower() == "y":
                self.__price = new_price
                print(f"Цена успешно изменена на {self.__price}")
            else:
                print("Операция изменения цены отменена")
        else:
            # Повышение или равна - просто меняем
            self.__price = new_price
            print(f"Цена успешно изменена на {self.__price}")

    def __str__(self):
        """Строковое представление продукта"""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Магический метод для сложения продуктов (получение общей стоимости)"""
        if isinstance(other, Product):
            # Общая стоимость текущего товара + общая стоимость другого товара
            total_cost = (self.__price * self.quantity) + (other.__price * other.quantity)
            return total_cost
        else:
            raise TypeError("Сложение возможно только с объектами класса Product")

    @classmethod
    def new_product(cls, product_dict, existing_products=None):
        """Класс-метод для создания объекта Product из словаря с проверкой дубликатов"""
        new_name = product_dict["name"]
        new_description = product_dict["description"]
        new_price = product_dict["price"]
        new_quantity = product_dict["quantity"]

        # Если список существующих товаров не передан или пуст, просто создаем новый товар
        if not existing_products:
            return cls(new_name, new_description, new_price, new_quantity)

        # Ищем товар с таким же именем
        for existing_product in existing_products:
            if existing_product.name == new_name:
                # Товар существует - обновляем количество и цену
                existing_product.quantity += new_quantity

                # Выбираем более высокую цену (через сеттер)
                if new_price > existing_product.price:
                    existing_product.price = new_price
                elif new_price < existing_product.price:
                    # При понижении цены также запрашивается подтверждение через сеттер
                    existing_product.price = new_price

                # Возвращаем существующий товар (обновленный)
                return existing_product

        # Если товар не найден, создаем новый
        return cls(new_name, new_description, new_price, new_quantity)
