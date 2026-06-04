from src.category import Category


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
