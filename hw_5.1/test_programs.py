import pytest
from programs import sum_even_numbers

# Позитивные тесты
def test_positive_even_numbers():
    assert sum_even_numbers([2, 4, 6, 8, 10]) == 30

def test_mixed_even_odd_positive():
    assert sum_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 30

def test_mixed_positive_negative_even_sum_positive():
    assert sum_even_numbers([10, -2, 8, -4, 6, 100]) == 118

def test_zero_in_list():
    assert sum_even_numbers([0, 2, 4, 6]) == 12

def test_only_zero():
    assert sum_even_numbers([0]) == 0

def test_large_positive_numbers():
    assert sum_even_numbers([20000, 19998, 20000]) == 59998

def test_sum_exactly_zero():
    assert sum_even_numbers([2, -2, 4, -4]) == 0

def test_single_positive_even():
    assert sum_even_numbers([42]) == 42

def test_large_list():
    large_list = list(range(0, 2000, 2))
    expected = sum(range(0, 2000, 2))
    assert sum_even_numbers(large_list) == expected

# Негативные тесты
def test_all_negative_even():
    assert sum_even_numbers([-2, -4, -6, -8]) == 1

def test_more_negative_than_positive():
    assert sum_even_numbers([2, -10, 4, -20, -30]) == 1

def test_negative_even_with_odd():
    assert sum_even_numbers([-1, -2, -3, -4]) == 1

def test_single_negative_even():
    assert sum_even_numbers([-100]) == 1

def test_sum_minus_one():
    assert sum_even_numbers([-2, 1]) == 1

def test_minimum_values():
    assert sum_even_numbers([-20000, -19998, -20000]) == 1

def test_large_negative_sum():
    assert sum_even_numbers([-20000] * 1000) == 1

# Граничные тесты
def test_empty_list():
    assert sum_even_numbers([]) == 0

def test_only_odd_numbers():
    assert sum_even_numbers([1, 3, 5, 7, 9]) == 0

def test_only_negative_odd():
    assert sum_even_numbers([-1, -3, -5, -7]) == 0

def test_balance_negative_and_positive():
    assert sum_even_numbers([-1000, 5000, 3000]) == 7000



