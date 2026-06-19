from src.category import Category
from src.product import Product


def test_category_init(category1: Category, category2: Category) -> None:
    assert category1.name == "Смартфоны"
    assert (
        category1.description == "Смартфоны, как средство не только коммуникации, "
        "но и получения дополнительных функций для удобства жизни"
    )
    assert category2.name == "Телевизоры"
    assert (
        category2.description == "Современный телевизор, который позволяет наслаждаться просмотром, "
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
    Category("Пусто", "Описание")
    assert Category.category_count == 1
    assert Category.product_count == 0

    # Создаем категорию с одним товаром
    product = Product("Тест", "Описание", 100.0, 2)
    Category("С товаром", "Описание", [product])
    assert Category.category_count == 2
    assert Category.product_count == 1

    # Создаем категорию с двумя товарами
    product2 = Product("Тест2", "Описание2", 200.0, 3)
    Category("С двумя товарами", "Описание", [product, product2])
    assert Category.category_count == 3
    assert Category.product_count == 3


def test_category_str(category1: Category) -> None:
    """Тест строкового представления категории"""
    expected = "Смартфоны, количество продуктов: 27 шт."  # 5 + 8 + 14 = 27
    assert str(category1) == expected


def test_category_str_empty() -> None:
    """Тест строкового представления пустой категории"""
    category = Category("Пустая категория", "Описание")
    expected = "Пустая категория, количество продуктов: 0 шт."
    assert str(category) == expected


def test_get_products_returns_copy(category1: Category) -> None:
    """Тест метода get_products, который возвращает копию списка"""
    products_copy = category1.get_products()
    original_products = category1._Category__products

    # Проверяем, что содержимое совпадает
    assert len(products_copy) == len(original_products)
    assert products_copy == original_products

    # Проверяем, что это разные объекты (копия)
    assert products_copy is not original_products

    # Изменяем копию и проверяем, что оригинал не изменился
    products_copy.append(Product("New", "Desc", 100, 1))
    assert len(products_copy) == len(original_products) + 1
    assert len(category1._Category__products) == len(original_products)


def test_get_products_empty() -> None:
    """Тест метода get_products для пустой категории"""
    category = Category("Пустая", "Описание")
    products = category.get_products()
    assert products == []
    assert products is not category._Category__products


def test_add_product_updates_product_count(category1: Category) -> None:
    """Тест обновления счетчика товаров при добавлении"""
    initial_count = Category.product_count
    product = Product("New Phone", "Desc", 50000, 2)

    category1.add_product(product)

    assert Category.product_count == initial_count + 1
    assert len(category1._Category__products) == 4  # Было 3, стало 4


def test_product_count_not_affected_by_get_products(category1: Category) -> None:
    """Тест, что получение копии продуктов не влияет на счетчик"""
    initial_count = Category.product_count

    _ = category1.get_products()
    _ = category1.products

    assert Category.product_count == initial_count
    assert len(category1._Category__products) == 3


def test_multiple_categories_share_counters() -> None:
    """Тест, что счетчики общие для всех категорий"""
    Category.category_count = 0
    Category.product_count = 0

    cat1 = Category("Cat1", "Desc", [Product("P1", "D1", 100, 1)])
    assert Category.category_count == 1
    assert Category.product_count == 1
    assert cat1.name == "Cat1"  # Используем переменную

    cat2 = Category("Cat2", "Desc", [])
    assert Category.category_count == 2
    assert Category.product_count == 1
    assert cat2.name == "Cat2"  # Используем переменную

    cat2.add_product(Product("P2", "D2", 200, 2))
    assert Category.category_count == 2
    assert Category.product_count == 2
