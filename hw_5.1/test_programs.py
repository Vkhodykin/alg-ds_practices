import pytest
from programs import sum_even_numbers
from programs import most_common_element
from programs import sum_two_indexes


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


# Позитивные тесты
def test_single_element():
    assert most_common_element([42]) == 42

def test_all_elements_same():
    assert most_common_element([5, 5, 5, 5, 5]) == 5

def test_one_clear_winner():
    assert most_common_element([1, 2, 2, 2, 3, 4]) == 2

def test_multiple_winners_return_smallest():
    assert most_common_element([1, 1, 2, 2, 3, 3]) == 1

def test_two_winners_smallest_first():
    assert most_common_element([10, 10, 20, 20, 30]) == 10

def test_all_unique_elements():
    assert most_common_element([5, 4, 3, 2, 1]) == 1

def test_unsorted_input():
    assert most_common_element([3, 1, 4, 1, 5, 9, 2, 1]) == 1

def test_negative_numbers():
    assert most_common_element([-1, -2, -2, -3, -2, -4]) == -2

def test_large_numbers():
    assert most_common_element([10000, 20000, 10000, 15000, 20000, 20000]) == 20000

def test_zero_values():
    assert most_common_element([0, 0, 1, 2, 0, 3]) == 0

def test_tie_with_three_elements():
    assert most_common_element([1, 1, 2, 2, 2, 3, 3]) == 2

def test_one_element_appears_more_than_half():
    assert most_common_element([3, 3, 3, 3, 1, 2, 3]) == 3

def test_mixed_positive_negative():
    assert most_common_element([-5, 3, -5, 7, -5, 3, 3]) == -5

def test_element_with_max_frequency_at_end():
    assert most_common_element([1, 2, 3, 4, 5, 5, 5, 5]) == 5

def test_element_with_max_frequency_at_beginning():
    assert most_common_element([5, 5, 5, 5, 1, 2, 3, 4]) == 5

# Негативные тесты
def test_empty_list_returns_none():
    assert most_common_element([]) is None

def test_complex_tie_smallest_not_first():
    result = most_common_element([10, 10, 5, 5, 5, 10, 10, 5])
    expected = 5
    assert result == expected
    assert result < 10

def test_tie_with_alternating_pattern():
    result = most_common_element([1, 2, 1, 2, 1, 2, 3])
    expected = 1
    assert result == expected

# Граничные тесты
def test_two_elements_different():
    assert most_common_element([1, 2]) == 1

def test_two_elements_same():
    assert most_common_element([7, 7]) == 7

def test_tie_at_beginning_and_end():
    assert most_common_element([5, 5, 1, 2, 3, 4, 5, 5]) == 5

def test_single_element_zero():
    assert most_common_element([0]) == 0

def test_minimum_values_range():
    assert most_common_element([1, 1, 1, 2, 2]) == 1

def test_maximum_values_range():
    assert most_common_element([20000, 20000, 20000, 19999, 19999]) == 20000

def test_alternating_tie_with_larger_numbers():
    result = most_common_element([1000, 2000, 1000, 2000, 3000])
    expected = 1000
    assert result == expected

def test_three_elements_all_unique():
    assert most_common_element([100, 200, 300]) == 100

def test_two_elements_with_zero():
    assert most_common_element([0, 1]) == 0

def test_consecutive_duplicates():
    assert most_common_element([1, 1, 1, 2, 2, 3, 3, 3, 3]) == 3


# Позитивные тесты
def test_basic_case():
    result = sum_two_indexes([2, 7, 11, 15], 9)
    assert result == [0, 1]

def test_numbers_at_end():
    result = sum_two_indexes([1, 2, 3, 4, 5, 6], 11)
    assert result == [4, 5]

def test_numbers_at_beginning():
    result = sum_two_indexes([10, 20, 30, 40, 50], 30)
    assert result == [0, 1]

def test_with_negative_numbers():
    result = sum_two_indexes([-3, 4, 3, 90], 0)
    assert result == [0, 2]

def test_with_zero():
    result = sum_two_indexes([0, 5, 10, 15], 5)
    assert result == [0, 1]

def test_duplicate_numbers():
    result = sum_two_indexes([3, 3, 4, 5], 6)
    assert result == [0, 1]

def test_target_is_zero():
    result = sum_two_indexes([-5, 5, 10, 20], 0)
    assert result == [0, 1]

def test_large_numbers():
    result = sum_two_indexes([10000, 20000, 30000, 40000], 30000)
    assert result == [0, 1]

def test_negative_target():
    result = sum_two_indexes([-10, -20, 5, 15], -30)
    assert result == [0, 1]

def test_mixed_positive_negative():
    result = sum_two_indexes([-1, -2, 3, 5, 8], 1)
    assert result == [1, 2]

# Негативные тесты
def test_no_solution_simple():
    result = sum_two_indexes([1, 2, 3, 4], 100)
    assert result is None

def test_no_solution_with_negative():
    result = sum_two_indexes([-5, -3, -1, 2], 10)
    assert result is None

def test_single_element():
    result = sum_two_indexes([42], 42)
    assert result is None

def test_empty_list():
    result = sum_two_indexes([], 5)
    assert result is None

def test_two_elements_no_match():
    result = sum_two_indexes([10, 20], 40)
    assert result is None

# Граничные тесты
def test_two_elements_match():
    result = sum_two_indexes([5, 5], 10)
    assert result == [0, 1]

def test_first_and_last():
    result = sum_two_indexes([1, 2, 3, 4, 5, 6], 7)
    assert result == [0, 5]

def test_adjacent_elements():
    result = sum_two_indexes([100, 200, 300, 400], 400)
    assert result == [0, 2]

def test_same_value_multiple_occurrences():
    result = sum_two_indexes([5, 5, 5, 5], 10)
    assert result == [0, 1]

def test_target_at_beginning_and_end():
    result = sum_two_indexes([1, 100, 200, 300, 400, 1], 2)
    assert result == [0, 5]

def test_with_large_negative_numbers():
    result = sum_two_indexes([-10000, -20000, 30000], -30000)
    assert result == [0, 1]

def test_zero_target_with_zeros():
    result = sum_two_indexes([0, 5, 0, 10], 0)
    assert result == [0, 2]

def test_max_value_range():
    result = sum_two_indexes([20000, 20000, 1, 2], 40000)
    assert result == [0, 1]

def test_min_value_range():
    result = sum_two_indexes([-20000, -20000, 1, 2], -40000)
    assert result == [0, 1]
