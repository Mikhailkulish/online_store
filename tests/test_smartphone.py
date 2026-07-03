def test_init_smartphone(smartphones1):
    assert smartphones1.name == "Samsung Galaxy S23 Ultra"
    assert smartphones1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphones1.price == 180000.0
    assert smartphones1.quantity == 5
    assert smartphones1.efficiency == 95.5
    assert smartphones1.model == "S23 Ultra"
    assert smartphones1.memory == 256
    assert smartphones1.color == "Серый"
