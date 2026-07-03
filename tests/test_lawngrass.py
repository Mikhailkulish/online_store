def test_init_lawngrass(lawngrasses1):
    assert lawngrasses1.name == "Газонная трава"
    assert lawngrasses1.description == "Элитная трава для газона"
    assert lawngrasses1.price == 500.0
    assert lawngrasses1.quantity == 20
    assert lawngrasses1.country == "Россия"
    assert lawngrasses1.germination_period == "7 дней"
    assert lawngrasses1.color == "Зеленый"
