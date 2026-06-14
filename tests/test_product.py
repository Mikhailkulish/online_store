from src.product import Product


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


def test_price_setter_decrease_approved(monkeypatch) -> None:
    product = Product("Test", "Desc", 100, 1)
    monkeypatch.setattr('builtins.input', lambda _: 'y')
    product.price = 80
    assert product.price == 80


def test_price_setter_decrease_cancelled(monkeypatch) -> None:
    product = Product("Test", "Desc", 100, 1)
    monkeypatch.setattr('builtins.input', lambda _: 'n')
    product.price = 80
    assert product.price == 100


def test_price_setter_increase() -> None:
    product = Product("Test", "Desc", 100, 1)
    product.price = 150
    assert product.price == 150


def test_new_product_no_existing() -> None:
    data = {'name': 'Iphone', 'description': 'New', 'price': 50000, 'quantity': 3}
    product = Product.new_product(data)
    assert product.name == 'Iphone'
    assert product.price == 50000
    assert product.quantity == 3


def test_new_product_duplicate_update_quantity() -> None:
    existing = Product("Phone", "Desc", 100, 5)
    data = {'name': 'Phone', 'description': 'Desc', 'price': 100, 'quantity': 3}
    result = Product.new_product(data, [existing])
    assert result.quantity == 8


def test_new_product_duplicate_higher_price() -> None:
    existing = Product("Phone", "Desc", 100, 5)
    data = {'name': 'Phone', 'description': 'Desc', 'price': 150, 'quantity': 3}
    result = Product.new_product(data, [existing])
    assert result.price == 150


def test_new_product_duplicate_lower_price(monkeypatch) -> None:
    existing = Product("Phone", "Desc", 100, 5)
    data = {'name': 'Phone', 'description': 'Desc', 'price': 80, 'quantity': 3}
    monkeypatch.setattr('builtins.input', lambda _: 'y')
    result = Product.new_product(data, [existing])
    assert result.price == 80
