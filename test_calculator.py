# test_calculator.py

from calculator import add, subtract

def test_add():
    assert add(3, 4) == 7
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(-1, -1) == 0
    assert subtract(2, 3) == -1
