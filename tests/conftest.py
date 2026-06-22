import pytest

from src.category import Category
from src.lawngrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


@pytest.fixture
def product1():
    return Product(
        name="Samsung Galaxy S23 Ultra", description="256GB, Серый цвет, 200MP камера", price=180000.0, quantity=5
    )


@pytest.fixture
def product2():
    return Product(name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8)


@pytest.fixture
def category1():
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, "
        "но и получения дополнительных функций для удобства жизни",
        products=[
            Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
            Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14),
        ],
    )


@pytest.fixture
def category2():
    return Category(
        name="Телевизоры",
        description="Современный телевизор, который позволяет наслаждаться просмотром, "
        "станет вашим другом и помощником",
        products=[Product('55" QLED 4K', "Фоновая подсветка", 1230000.0, 7)],
    )


@pytest.fixture
def product3():
    """Продукт для тестирования операций"""
    return Product(name="Test Product", description="Test description", price=150.0, quantity=10)


@pytest.fixture
def product_dict():
    """Словарь для тестирования new_product"""
    return {"name": "TestPhone", "description": "New phone", "price": 25000.0, "quantity": 4}


@pytest.fixture
def empty_category():
    """Пустая категория для тестирования"""
    return Category(name="Пустая категория", description="Категория без товаров")


@pytest.fixture
def single_product_category():
    """Категория с одним товаром"""
    product = Product("Single Phone", "Desc", 15000, 3)
    return Category(name="Один товар", description="Категория с одним товаром", products=[product])


@pytest.fixture
def smartphones1():
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture
def smartphones2():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def lawngrasses1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
