from src.utils import is_positive


def test_positive_number():
    assert is_positive(10) == True


def test_negative_number():
    assert is_positive(-5) == False


def test_zero():
    assert is_positive(0) == False