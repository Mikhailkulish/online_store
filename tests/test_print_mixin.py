from src.lawngrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def test_print_mixin_output(capsys):
    """Тест: проверка вывода PrintMixin при создании объекта"""
    # Создаем объект - вывод должен произойти автоматически
    _ = Product("Test Product", "Test Description", 1000.0, 5)

    # Захватываем вывод
    captured = capsys.readouterr()

    # Проверяем, что вывод не пустой
    assert captured.out != ""

    expected = "Product('Test Product', 'Test Description', 1000.0, 5)\n"
    assert captured.out == expected


def test_print_mixin_output_with_kwargs(capsys):
    """Тест: проверка вывода PrintMixin с именованными аргументами"""
    # Создаем продукт через new_product с kwargs
    product_dict = {"name": "Test", "description": "Desc", "price": 100, "quantity": 2}
    _ = Product.new_product(product_dict)
    captured = capsys.readouterr()
    # Проверяем, что вывод содержит информацию о создании
    assert "Product('Test', 'Desc', 100, 2)" in captured.out


def test_print_mixin_for_smartphone(capsys):
    """Тест: проверка вывода PrintMixin для дочернего класса Smartphone"""
    _ = Smartphone("iPhone", "Smartphone", 1000.0, 5, "A15", "15 Pro", "256GB", "Black")
    captured = capsys.readouterr()
    expected = "Smartphone('iPhone', 'Smartphone', 1000.0, 5, 'A15', '15 Pro', '256GB', 'Black')\n"
    assert captured.out == expected


def test_print_mixin_for_lawngrass(capsys):
    """Тест: проверка вывода PrintMixin для дочернего класса LawnGrass"""
    _ = LawnGrass("Трава", "Газонная трава", 500.0, 10, "Россия", "30 дней", "Зеленый")
    captured = capsys.readouterr()
    expected = "LawnGrass('Трава', 'Газонная трава', 500.0, 10, 'Россия', '30 дней', 'Зеленый')\n"
    assert captured.out == expected


def test_print_mixin_repr_method():
    """Тест: проверка метода __repr__ у объекта с миксином"""
    product = Product("Test", "Description", 200.0, 3)
    expected = "Product('Test', 'Description', 200.0, 3)"
    assert repr(product) == expected


def test_print_mixin_multiple_objects(capsys):
    """Тест: проверка вывода при создании нескольких объектов"""
    _ = Product("Product1", "Desc1", 100.0, 1)
    _ = Product("Product2", "Desc2", 200.0, 2)
    captured = capsys.readouterr()

    # Проверяем, что оба объекта были выведены
    output_lines = captured.out.strip().split("\n")
    assert len(output_lines) == 2
    assert "Product('Product1', 'Desc1', 100.0, 1)" in output_lines[0]
    assert "Product('Product2', 'Desc2', 200.0, 2)" in output_lines[1]


def test_print_mixin_inheritance():
    """Тест: проверка, что миксин работает через наследование"""
    # Создаем объект и проверяем наличие атрибутов от миксина
    product = Product("Test", "Desc", 300.0, 4)

    # Проверяем, что у объекта есть атрибуты, добавленные миксином
    assert hasattr(product, "_args")
    assert hasattr(product, "_kwargs")

    # Проверяем, что параметры сохранились корректно
    assert product._args == ("Test", "Desc", 300.0, 4)
    assert product._kwargs == {}


def test_print_mixin_with_price_change(capsys):
    """Тест: проверка, что миксин не мешает работе сеттера цены"""
    product = Product("Test", "Desc", 100.0, 1)
    captured = capsys.readouterr()  # Очищаем вывод от создания

    # Меняем цену
    product.price = 150.0
    captured = capsys.readouterr()
    assert "Цена успешно изменена на 150.0" in captured.out

    # Проверяем, что цена изменилась
    assert product.price == 150.0


def test_print_mixin_dunder_methods():
    """Тест: проверка, что миксин не мешает другим магическим методам"""
    product1 = Product("Test1", "Desc1", 100.0, 2)
    product2 = Product("Test2", "Desc2", 200.0, 3)

    # Проверяем __add__
    total = product1 + product2
    assert total == (100.0 * 2) + (200.0 * 3)  # 200 + 600 = 800

    # Проверяем __str__
    assert str(product1) == "Test1, 100.0 руб. Остаток: 2 шт."


def test_print_mixin_private_attribute():
    """Тест: проверка работы миксина с приватными атрибутами"""
    product = Product("Test", "Desc", 500.0, 5)

    # Проверяем, что приватный атрибут __price доступен через свойство
    assert product.price == 500.0

    # Проверяем, что миксин сохранил параметры (без приватных атрибутов)
    assert product._args == ("Test", "Desc", 500.0, 5)


def test_print_mixin_repr_after_price_change():
    """Тест: проверка repr после изменения цены"""
    product = Product("Test", "Desc", 100.0, 2)

    # Меняем цену
    product.price = 200.0

    # repr должен показывать начальные параметры, а не текущее состояние
    expected = "Product('Test', 'Desc', 100.0, 2)"
    assert repr(product) == expected
