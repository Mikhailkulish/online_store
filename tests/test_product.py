import pytest

from src.base_product import BaseProduct
from src.lawngrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def test_product_init(product1: Product) -> None:
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 5


def test_product_init_with_zero_quantity() -> None:
    """Тест: создание продукта с нулевым количеством должно вызывать ValueError"""
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product("Test", "Description", 100.0, 0)


def test_price_setter_invalid() -> None:
    product = Product("Test", "Desc", 100, 1)
    product.price = -50
    assert product.price == 100
    product.price = 0
    assert product.price == 100


def test_product_str(product1: Product) -> None:
    """Тест строкового представления продукта"""
    expected = "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert str(product1) == expected


def test_product_add_same_type(product1: Product, product2: Product) -> None:
    """Тест магического метода __add__ для сложения двух продуктов"""
    total = product1 + product2
    expected = (180000.0 * 5) + (210000.0 * 8)  # 900000 + 1680000 = 2580000
    assert total == expected


def test_product_add_different_type(product1: Product) -> None:
    """Тест магического метода __add__ с другим типом данных"""
    with pytest.raises(TypeError, match="Сложение возможно только с объектами класса Product"):
        _ = product1 + "some string"


def test_price_getter(product1: Product) -> None:
    """Тест геттера для получения цены"""
    assert product1.price == 180000.0


def test_new_product_duplicate_same_price() -> None:
    """Тест обновления существующего товара с такой же ценой"""
    existing = Product("Phone", "Desc", 100, 5)
    data = {"name": "Phone", "description": "Desc", "price": 100, "quantity": 3}
    result = Product.new_product(data, [existing])
    assert result.price == 100
    assert result.quantity == 8


def test_new_product_no_existing_products_empty_list() -> None:
    """Тест создания нового продукта при пустом списке существующих"""
    data = {"name": "NewPhone", "description": "Brand new", "price": 30000, "quantity": 2}
    product = Product.new_product(data, [])
    assert product.name == "NewPhone"
    assert product.price == 30000
    assert product.quantity == 2


def test_new_product_duplicate_lower_price_cancelled(monkeypatch) -> None:
    """Тест обновления существующего товара с более низкой ценой (отмена)"""
    existing = Product("Phone", "Desc", 100, 5)
    data = {"name": "Phone", "description": "Desc", "price": 80, "quantity": 3}
    monkeypatch.setattr("builtins.input", lambda _: "n")
    result = Product.new_product(data, [existing])
    assert result.price == 100  # Цена не изменилась
    assert result.quantity == 8  # Количество обновилось


def test_new_product_duplicate_higher_price_no_prompt() -> None:
    """Тест обновления существующего товара с более высокой ценой (без запроса)"""
    existing = Product("Phone", "Desc", 100, 5)
    data = {"name": "Phone", "description": "Desc", "price": 200, "quantity": 3}
    result = Product.new_product(data, [existing])
    assert result.price == 200  # Цена повысилась без запроса
    assert result.quantity == 8


def test_price_setter_decrease_approved(monkeypatch) -> None:
    product = Product("Test", "Desc", 100, 1)
    monkeypatch.setattr("builtins.input", lambda _: "y")
    product.price = 80
    assert product.price == 80


def test_price_setter_decrease_cancelled(monkeypatch) -> None:
    product = Product("Test", "Desc", 100, 1)
    monkeypatch.setattr("builtins.input", lambda _: "n")
    product.price = 80
    assert product.price == 100


def test_price_setter_increase() -> None:
    product = Product("Test", "Desc", 100, 1)
    product.price = 150
    assert product.price == 150


def test_new_product_no_existing() -> None:
    data = {"name": "Iphone", "description": "New", "price": 50000, "quantity": 3}
    product = Product.new_product(data)
    assert product.name == "Iphone"
    assert product.price == 50000
    assert product.quantity == 3


def test_new_product_duplicate_update_quantity() -> None:
    existing = Product("Phone", "Desc", 100, 5)
    data = {"name": "Phone", "description": "Desc", "price": 100, "quantity": 3}
    result = Product.new_product(data, [existing])
    assert result.quantity == 8


def test_new_product_duplicate_higher_price() -> None:
    existing = Product("Phone", "Desc", 100, 5)
    data = {"name": "Phone", "description": "Desc", "price": 150, "quantity": 3}
    result = Product.new_product(data, [existing])
    assert result.price == 150


def test_new_product_duplicate_lower_price(monkeypatch) -> None:
    existing = Product("Phone", "Desc", 100, 5)
    data = {"name": "Phone", "description": "Desc", "price": 80, "quantity": 3}
    monkeypatch.setattr("builtins.input", lambda _: "y")
    result = Product.new_product(data, [existing])
    assert result.price == 80


def test_product_add_same_type_new(product1: Product, product2: Product) -> None:
    """Тест магического метода __add__ для сложения двух продуктов"""
    total = product1 + product2
    expected = (180000.0 * 5) + (210000.0 * 8)  # 900000 + 1680000 = 2580000
    assert total == expected


def test_product_add_different_type_new(product1: Product) -> None:
    """Тест магического метода __add__ с другим типом данных"""
    with pytest.raises(TypeError, match="Сложение возможно только с объектами класса Product"):
        _ = product1 + "some string"


def test_product_add_different_product_classes(product1: Product, smartphones1: Smartphone) -> None:
    """Тест: попытка сложить товары разных классов должна вызывать TypeError"""
    with pytest.raises(TypeError, match="Нельзя складывать товары разных классов"):
        _ = product1 + smartphones1


def test_product_add_different_subclasses(smartphones1: Smartphone, lawngrasses1: LawnGrass) -> None:
    """Тест: попытка сложить товары разных наследников Product"""
    with pytest.raises(TypeError, match="Нельзя складывать товары разных классов"):
        _ = smartphones1 + lawngrasses1


def test_product_add_same_subclass(smartphones1: Smartphone, smartphones2: Smartphone) -> None:
    """Тест: сложение товаров одного класса-наследника должно работать"""
    total = smartphones1 + smartphones2
    expected = (180000.0 * 5) + (210000.0 * 8)
    assert total == expected


def test_product_with_mixin_attributes():
    """Тест: проверка, что объект Product имеет атрибуты от миксина"""
    product = Product("Test", "Desc", 100.0, 5)

    # Проверяем наличие атрибутов от PrintMixin
    assert hasattr(product, "_args"), "Объект должен иметь атрибут _args от PrintMixin"
    assert hasattr(product, "_kwargs"), "Объект должен иметь атрибут _kwargs от PrintMixin"

    # Проверяем, что параметры сохранились корректно
    assert product._args == ("Test", "Desc", 100.0, 5)
    assert product._kwargs == {}


def test_product_with_mixin_repr():
    """Тест: проверка метода __repr__ у Product с миксином"""
    product = Product("Test", "Desc", 200.0, 3)
    expected = "Product('Test', 'Desc', 200.0, 3)"
    assert repr(product) == expected


def test_product_with_mixin_str_not_affected():
    """Тест: проверка, что __str__ не изменился из-за миксина"""
    product = Product("Test", "Desc", 150.0, 7)
    expected = "Test, 150.0 руб. Остаток: 7 шт."
    assert str(product) == expected


def test_product_with_mixin_price_getter():
    """Тест: проверка, что геттер цены работает с миксином"""
    product = Product("Test", "Desc", 300.0, 2)
    assert product.price == 300.0


def test_product_with_mixin_price_setter(capsys, monkeypatch):
    """Тест: проверка, что сеттер цены работает с миксином (без конфликтов)"""
    product = Product("Test", "Desc", 100.0, 1)

    # Очищаем вывод от создания объекта
    capsys.readouterr()

    # Повышаем цену
    product.price = 150.0
    captured = capsys.readouterr()
    assert "Цена успешно изменена на 150.0" in captured.out
    assert product.price == 150.0

    # Понижаем цену с подтверждением
    monkeypatch.setattr("builtins.input", lambda _: "y")
    product.price = 80.0
    captured = capsys.readouterr()
    assert "Цена успешно изменена на 80.0" in captured.out
    assert product.price == 80.0


def test_product_with_mixin_add_operation():
    """Тест: проверка, что __add__ работает с миксином"""
    product1 = Product("Product1", "Desc1", 100.0, 2)
    product2 = Product("Product2", "Desc2", 200.0, 3)

    total = product1 + product2
    expected = (100.0 * 2) + (200.0 * 3)  # 200 + 600 = 800
    assert total == expected


def test_product_with_mixin_new_product():
    """Тест: проверка, что new_product работает с миксином"""
    data = {"name": "NewPhone", "description": "Brand new", "price": 30000, "quantity": 2}
    product = Product.new_product(data)

    assert product.name == "NewPhone"
    assert product.price == 30000
    assert product.quantity == 2

    # Проверяем, что миксин сохранил параметры
    assert product._args == ("NewPhone", "Brand new", 30000, 2)


def test_product_with_mixin_new_product_duplicate():
    """Тест: проверка new_product с дубликатами (миксин не должен мешать)"""
    existing = Product("Phone", "Desc", 100, 5)
    data = {"name": "Phone", "description": "Desc", "price": 200, "quantity": 3}

    result = Product.new_product(data, [existing])

    # Проверяем, что количество обновилось
    assert result.quantity == 8
    # Проверяем, что цена повысилась
    assert result.price == 200


def test_product_with_mixin_multiple_operations(capsys):
    """Тест: проверка нескольких операций с одним объектом"""
    product = Product("Test", "Desc", 100.0, 5)

    # Очищаем вывод от создания
    capsys.readouterr()

    # Выполняем несколько операций
    assert product.price == 100.0
    assert str(product) == "Test, 100.0 руб. Остаток: 5 шт."

    product.price = 150.0
    captured = capsys.readouterr()
    assert "Цена успешно изменена на 150.0" in captured.out
    assert product.price == 150.0

    # Проверяем, что миксин не потерял параметры
    assert product._args == ("Test", "Desc", 100.0, 5)


def test_product_with_mixin_inheritance_in_subclass():
    """Тест: проверка, что миксин работает в иерархии наследования"""
    # Создаем Smartphone (проверяем, что миксин работает через наследование)
    smartphone = Smartphone("iPhone", "Smartphone", 1000.0, 5, "A15", "15 Pro", "256GB", "Black")

    # Проверяем наличие атрибутов от миксина
    assert hasattr(smartphone, "_args")
    assert hasattr(smartphone, "_kwargs")

    # Проверяем, что все параметры сохранились
    expected_args = ("iPhone", "Smartphone", 1000.0, 5, "A15", "15 Pro", "256GB", "Black")
    assert smartphone._args == expected_args

    # Проверяем, что атрибуты Smartphone сохранились
    assert smartphone.efficiency == "A15"
    assert smartphone.model == "15 Pro"
    assert smartphone.memory == "256GB"
    assert smartphone.color == "Black"


def test_product_with_mixin_repr_subclass():
    """Тест: проверка __repr__ для дочернего класса"""
    smartphone = Smartphone("iPhone", "Smartphone", 1000.0, 5, "A15", "15 Pro", "256GB", "Black")
    expected = "Smartphone('iPhone', 'Smartphone', 1000.0, 5, 'A15', '15 Pro', '256GB', 'Black')"
    assert repr(smartphone) == expected


def test_product_with_mixin_private_attribute_access():
    """Тест: проверка доступа к приватному атрибуту через свойства"""
    product = Product("Test", "Desc", 500.0, 10)

    # Прямой доступ к приватному атрибуту невозможен
    with pytest.raises(AttributeError):
        _ = product.__price

    # Доступ через свойство работает
    assert product.price == 500.0

    # Проверяем, что миксин не хранит приватный атрибут
    assert "__price" not in product._args


def test_product_with_mixin_equality_operations():
    """Тест: проверка, что миксин не влияет на сравнение объектов"""
    product1 = Product("Test", "Desc", 100.0, 5)
    product2 = Product("Test", "Desc", 100.0, 5)

    # Проверяем, что объекты разные (несмотря на одинаковые значения)
    assert product1 is not product2

    # Проверяем, что __add__ работает
    assert product1 + product2 == 1000.0  # 100 * 5 + 100 * 5 = 1000


def test_product_with_mixin_type_checking():
    """Тест: проверка, что миксин не влияет на isinstance и type"""
    product = Product("Test", "Desc", 100.0, 5)
    smartphone = Smartphone("iPhone", "Smartphone", 1000.0, 5, "A15", "15 Pro", "256GB", "Black")

    # Проверяем типы
    assert isinstance(product, Product)
    assert isinstance(product, BaseProduct)
    assert isinstance(smartphone, Product)
    assert isinstance(smartphone, Smartphone)

    # Проверяем, что Product не является Smartphone
    assert not isinstance(product, Smartphone)


def test_product_with_mixin_mro():
    """Тест: проверка правильного порядка наследования (MRO)"""
    # Проверяем, что PrintMixin стоит перед BaseProduct в MRO
    mro = Product.__mro__
    mro_names = [cls.__name__ for cls in mro]

    # Проверяем порядок
    assert "Product" in mro_names
    assert "PrintMixin" in mro_names
    assert "BaseProduct" in mro_names

    # PrintMixin должен быть перед BaseProduct
    assert mro_names.index("PrintMixin") < mro_names.index("BaseProduct")


def test_product_with_mixin_no_side_effects():
    """Тест: проверка, что миксин не создает побочных эффектов"""
    product = Product("Test", "Desc", 100.0, 5)

    # Сохраняем начальное состояние
    initial_price = product.price
    initial_quantity = product.quantity

    # Вызываем repr (миксин должен только вернуть строку, не меняя состояние)
    repr_str = repr(product)

    # Проверяем, что состояние не изменилось
    assert product.price == initial_price
    assert product.quantity == initial_quantity
    assert product.name == "Test"
    assert product.description == "Desc"

    # Проверяем, что repr содержит правильную информацию
    assert "Product('Test', 'Desc', 100.0, 5)" in repr_str
