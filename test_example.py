import example


def test_add():
    assert example.add(1, 2) == 3
    assert example.add(0, 0) == 0
    assert example.add(-1, 1) == 0


def test_subtract():
    assert example.subtract(3, 2) == 1
    assert example.subtract(0, 0) == 0
    assert example.subtract(-1, -1) == 0
