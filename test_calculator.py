from calculator import add # Import the function to test

# Test function names MUST start with 'test_'
def test_add_positive_numbers():
    # Use simple 'assert' statements
    assert add(2, 3) == 5
    assert add(100, 1) == 101

def test_add_negative_numbers():
    assert add(-1, -1) == -2
    assert add(-5, 5) == 0
