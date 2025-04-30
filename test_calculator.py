from calculator import add  # Import the function to test
from calculator import subtract
from calculator import multiply

# Test function names MUST start with 'test_'


def test_add_positive_numbers():
    # Use simple 'assert' statements
    assert add(2, 3) == 5
    assert add(100, 1) == 101


def test_add_negative_numbers():
    assert add(-1, -1) == -2
    assert add(-5, 5) == 0


def test_subtract_numbers():
    assert subtract(2, 3) == -1
    assert subtract(200, 5) == 195
    assert subtract(3, 3) == 0
    assert subtract(5, 50) == -45


def test_subtract_negative_numbers():
    assert subtract(-1, 1) == -2
    assert subtract(1, -1) == 2
    assert subtract(5, -50) == 55


def test_multiply_numbers():
    assert multiply(1, 6) == 6
    assert multiply(3, 10) == 30
    assert multiply(-5, 5) == -25
