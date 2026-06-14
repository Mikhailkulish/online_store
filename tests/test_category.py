from src.category import Category
from src.product import Product


def test_category_init(category1: Category, category2: Category) -> None:
    assert category1.name == "Смартфоны"
    assert (
            category1.description
            == "Смартфоны, как средство не только коммуникации, "
               "но и получения дополнительных функций для удобства жизни"
    )
    assert category2.name == "Телевизоры"
    assert (
            category2.description
            == "Современный телевизор, который позволяет наслаждаться просмотром, "
               "станет вашим другом и помощником"
    )
    assert len(category1.products) == 3
    assert len(category2.products) == 1

    assert category1.category_count == 2
    assert category2.category_count == 2

    assert category1.product_count == 4
    assert category2.product_count == 4


def test_category_init_without_products():
    """Тест создания категории без товаров"""
    category = Category("Книги", "Интересные книги")

    assert category.name == "Книги"
    assert category.description == "Интересные книги"
    assert category.products == []
    assert category._Category__products == []  # проверка приватного атрибута


def test_products_getter_format(category1: Category):
    """Тест форматирования товаров в геттере"""
    products_list = category1.products

    assert len(products_list) == 3
    assert products_list[0] == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert products_list[1] == "Iphone 15, 210000.0 руб. Остаток: 8 шт."
    assert products_list[2] == "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."


def test_products_getter_empty():
    """Тест геттера для пустой категории"""
    category = Category("Пустая", "Без товаров")
    assert category.products == []


def test_add_product(category1: Category, product1: Product, product2: Product):
    """Тест добавления товара в категорию"""
    initial_product_count = Category.product_count
    initial_products_len = len(category1._Category__products)

    category1.add_product(product1)

    assert len(category1._Category__products) == initial_products_len + 1
    assert category1._Category__products[-1] == product1
    assert Category.product_count == initial_product_count + 1

    # Добавляем еще один товар
    category1.add_product(product2)
    assert len(category1._Category__products) == initial_products_len + 2
    assert Category.product_count == initial_product_count + 2


def test_category_counters_persistence():
    """Тест корректности счетчиков при создании нескольких категорий"""
    # Сбрасываем счетчики через присвоение новых значений (для чистоты теста)
    Category.category_count = 0
    Category.product_count = 0

    # Создаем пустую категорию
    category_empty = Category("Пусто", "Описание")
    assert Category.category_count == 1
    assert Category.product_count == 0  # товаров нет, счетчик не изменился

    # Создаем категорию с одним товаром
    product = Product("Тест", "Описание", 100.0, 2)
    category_with_product = Category("С товаром", "Описание", [product])
    assert Category.category_count == 2
    assert Category.product_count == 1  # Было 0, добавили 1 товар, стало 1

    # Создаем категорию с двумя товарами
    product2 = Product("Тест2", "Описание2", 200.0, 3)
    category_with_two_products = Category("С двумя товарами", "Описание", [product, product2])
    assert Category.category_count == 3
    assert Category.product_count == 3  # Было 1, добавили 2 товара, стало 3
