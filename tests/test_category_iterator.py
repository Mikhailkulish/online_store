import pytest
from src.category import Category
from src.category_iterator import CategoryIterator


def test_category_iterator_init(category1: Category) -> None:
    """Тест инициализации итератора"""
    iterator = CategoryIterator(category1)

    assert iterator.index == 0
    assert len(iterator.products) == 3
    assert iterator.products == category1.get_products()


def test_category_iterator_iter(category1: Category) -> None:
    """Тест метода __iter__, который возвращает сам итератор"""
    iterator = CategoryIterator(category1)

    # Проверяем, что __iter__ возвращает тот же объект
    assert iter(iterator) is iterator


def test_category_iterator_next(category1: Category) -> None:
    """Тест последовательного перебора товаров"""
    iterator = CategoryIterator(category1)
    products = category1.get_products()

    # Проверяем последовательный перебор
    assert next(iterator) == products[0]
    assert iterator.index == 1

    assert next(iterator) == products[1]
    assert iterator.index == 2

    assert next(iterator) == products[2]
    assert iterator.index == 3


def test_category_iterator_stop_iteration(category1: Category) -> None:
    """Тест возникновения исключения StopIteration при завершении перебора"""
    iterator = CategoryIterator(category1)
    products = category1.get_products()

    # Перебираем все элементы
    for _ in range(len(products)):
        next(iterator)

    # Следующий вызов должен вызвать StopIteration
    with pytest.raises(StopIteration):
        next(iterator)


def test_category_iterator_empty_category(empty_category: Category) -> None:
    """Тест итератора для пустой категории"""
    iterator = CategoryIterator(empty_category)

    assert iterator.products == []
    assert iterator.index == 0

    with pytest.raises(StopIteration):
        next(iterator)


def test_category_iterator_works_in_for_loop(category1: Category) -> None:
    """Тест использования итератора в цикле for"""
    iterator = CategoryIterator(category1)
    products = category1.get_products()

    result = []
    for product in iterator:
        result.append(product)

    assert result == products
    assert iterator.index == len(products)
