import pytest

from src.product import Product
from src.smartphone import Smartphone
from src.lawngrass import LawnGrass


def test_product_init(product1: Product) -> None:
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 5


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
