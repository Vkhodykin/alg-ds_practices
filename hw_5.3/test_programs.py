import pytest
from programs import max_in_range
from programs import rotate_and_reverse
from programs import reverse_even_elements
from programs import large_integer_plus_one

# Позитивные тесты
def test_max_in_range_positive_simple_range():
    arr = [1, 5, 3, 8, 2]
    assert max_in_range(arr, 1, 3) == (8, 3, 2)

def test_max_in_range_positive_max_at_start():
    arr = [10, 3, 7, 2, 5]
    assert max_in_range(arr, 1, 4) == (7, 2, 1)

def test_max_in_range_positive_max_at_end():
    arr = [4, 6, 2, 9, 1]
    assert max_in_range(arr, 0, 3) == (9, 3, 3)

def test_max_in_range_positive_multiple_maxima():
    arr = [5, 8, 3, 8, 2, 8]
    assert max_in_range(arr, 1, 5) == (8, 1, 0)

def test_max_in_range_positive_negative_numbers():
    arr = [-5, -2, -8, -1, -3]
    assert max_in_range(arr, 0, 4) == (-1, 3, 3)

def test_max_in_range_positive_mixed_numbers():
    arr = [-10, 5, -3, 8, -2, 0]
    assert max_in_range(arr, 2, 4) == (8, 3, 1)

def test_max_in_range_positive_float_numbers():
    arr = [1.5, 3.2, 2.8, 4.1, 2.5]
    assert max_in_range(arr, 0, 3) == (4.1, 3, 3)

def test_max_in_range_positive_single_element_range():
    arr = [42, 7, 15, 23]
    assert max_in_range(arr, 2, 2) == (15, 2, 0)

def test_max_in_range_positive_full_array():
    arr = [3, 7, 2, 9, 5]
    assert max_in_range(arr, 0, 4) == (9, 3, 3)

def test_max_in_range_positive_large_numbers():
    arr = [1000000, 999999, 1000001, 999998]
    assert max_in_range(arr, 0, 3) == (1000001, 2, 2)

# Негативные тесты
def test_max_in_range_negative_start_greater_than_end():
    arr = [1, 2, 3, 4, 5]
    with pytest.raises(ValueError, match= "Некорректные значения start и end"):
        max_in_range(arr, 3, 1)

def test_max_in_range_negative_start_negative():
    arr = [1, 2, 3, 4, 5]
    with pytest.raises(ValueError, match= "Некорректные значения start и end"):
        max_in_range(arr, -1, 3)

def test_max_in_range_negative_end_out_of_range():
    arr = [1, 2, 3, 4, 5]
    with pytest.raises(ValueError, match= "Некорректные значения start и end"):
        max_in_range(arr, 0, 10)

def test_max_in_range_negative_empty_array():
    arr = []
    with pytest.raises(ValueError, match= "Массив не может быть пустым"):
        max_in_range(arr, 0, 0)

def test_max_in_range_negative_start_equal_length():
    arr = [1, 2, 3]
    with pytest.raises(ValueError, match= "Некорректные значения start и end"):
        max_in_range(arr, 3, 3)

def test_max_in_range_negative_end_negative():
    arr = [1, 2, 3, 4, 5]
    with pytest.raises(ValueError, match= "Некорректные значения start и end"):
        max_in_range(arr, 0, -1)

def test_max_in_range_negative_start_greater_than_array_length():
    arr = [1, 2, 3]
    with pytest.raises(ValueError, match= "Некорректные значения start и end"):
        max_in_range(arr, 5, 6)

# Граничные тесты
def test_max_in_range_boundary_two_elements():
    arr = [10, 20]
    assert max_in_range(arr, 0, 1) == (20, 1, 1)

def test_max_in_range_boundary_start_zero():
    arr = [5, 2, 8, 1]
    assert max_in_range(arr, 0, 2) == (8, 2, 2)

def test_max_in_range_boundary_end_last_index():
    arr = [1, 3, 2, 4]
    assert max_in_range(arr, 1, 3) == (4, 3, 2)

def test_max_in_range_boundary_zero_based_indexing():
    arr = [100, 200, 300, 400, 500]
    assert max_in_range(arr, 2, 4) == (500, 4, 2)

def test_max_in_range_boundary_consecutive_equal_values():
    arr = [7, 7, 7, 7, 7]
    assert max_in_range(arr, 0, 4) == (7, 0, 0)


# Позитивные тесты
def test_rotate_and_reverse_positive_simple_rotation():
    arr = [1, 2, 3, 4, 5]
    assert rotate_and_reverse(arr, 2) == [3, 2, 1, 5, 4]

def test_rotate_and_reverse_positive_rotate_by_one():
    arr = [1, 2, 3, 4]
    assert rotate_and_reverse(arr, 1) == [3, 2, 1, 4]

def test_rotate_and_reverse_positive_rotate_by_three():
    arr = [1, 2, 3, 4, 5, 6]
    assert rotate_and_reverse(arr, 3) == [3, 2, 1, 6, 5, 4]

def test_rotate_and_reverse_positive_string_list():
    arr = ['a', 'b', 'c', 'd', 'e']
    assert rotate_and_reverse(arr, 2) == ['c', 'b', 'a', 'e', 'd']

def test_rotate_and_reverse_positive_mixed_types():
    arr = [1, 'two', 3.0, 'four', 5]
    assert rotate_and_reverse(arr, 1) == ['four', 3.0, 'two', 1, 5]

def test_rotate_and_reverse_positive_negative_numbers():
    arr = [-5, -4, -3, -2, -1]
    assert rotate_and_reverse(arr, 2) == [-3, -4, -5, -1, -2]

def test_rotate_and_reverse_positive_large_k():
    arr = [1, 2, 3, 4]
    assert rotate_and_reverse(arr, 6) == [2, 1, 4, 3]

def test_rotate_and_reverse_positive_very_large_k():
    arr = [10, 20, 30]
    assert rotate_and_reverse(arr, 100) == [20, 10, 30]

def test_rotate_and_reverse_positive_single_element():
    arr = [42]
    assert rotate_and_reverse(arr, 5) == [42]

def test_rotate_and_reverse_positive_two_elements():
    arr = [1, 2]
    assert rotate_and_reverse(arr, 1) == [1, 2]

# Негативные тесты
def test_rotate_and_reverse_negative_negative_k():
    arr = [1, 2, 3, 4, 5]
    result = rotate_and_reverse(arr, -2)
    assert result == [2, 1, 5, 4, 3]

def test_rotate_and_reverse_negative_large_negative_k():
    arr = [1, 2, 3]
    result = rotate_and_reverse(arr, -7)
    assert result == [1, 3, 2]

def test_rotate_and_reverse_negative_k_non_integer():
    arr = [1, 2, 3]
    with pytest.raises(TypeError):
        rotate_and_reverse(arr, 2.5)

def test_rotate_and_reverse_negative_k_none():
    arr = [1, 2, 3]
    with pytest.raises(TypeError):
        rotate_and_reverse(arr, None)

# Граничные тесты
def test_rotate_and_reverse_boundary_k_zero():
    arr = [1, 2, 3, 4, 5]
    assert rotate_and_reverse(arr, 0) == [5, 4, 3, 2, 1]

def test_rotate_and_reverse_boundary_k_equal_length():
    arr = [1, 2, 3, 4]
    assert rotate_and_reverse(arr, 4) == [4, 3, 2, 1]

def test_rotate_and_reverse_boundary_k_multiple_of_length():
    arr = [1, 2, 3]
    assert rotate_and_reverse(arr, 6) == [3, 2, 1]

def test_rotate_and_reverse_boundary_empty_list():
    arr = []
    assert rotate_and_reverse(arr, 5) == []

def test_rotate_and_reverse_boundary_large_list():
    arr = list(range(1000))
    result = rotate_and_reverse(arr, 250)
    assert len(result) == 1000
    assert sorted(result) == sorted(arr)


# Позитивные тесты
def test_reverse_even_elements_positive_mixed_numbers():
    arr = [1, 2, 3, 4, 5, 6]
    assert reverse_even_elements(arr) == [1, 6, 3, 4, 5, 2]

def test_reverse_even_elements_positive_all_even():
    arr = [2, 4, 6, 8, 10]
    assert reverse_even_elements(arr) == [10, 8, 6, 4, 2]

def test_reverse_even_elements_positive_all_odd():
    arr = [1, 3, 5, 7, 9]
    assert reverse_even_elements(arr) == [1, 3, 5, 7, 9]

def test_reverse_even_elements_positive_single_even():
    arr = [1, 2, 3, 5, 7]
    assert reverse_even_elements(arr) == [1, 2, 3, 5, 7]

def test_reverse_even_elements_positive_single_odd():
    arr = [2, 4, 6, 7, 8]
    assert reverse_even_elements(arr) == [8, 6, 4, 7, 2]

def test_reverse_even_elements_positive_negative_numbers():
    arr = [-4, -3, -2, -1, 0, 1, 2, 3]
    assert reverse_even_elements(arr) == [2, -3, 0, -1, -2, 1, -4, 3]

def test_reverse_even_elements_positive_duplicate_evens():
    arr = [2, 2, 3, 4, 4, 5, 6]
    assert reverse_even_elements(arr) == [6, 4, 3, 4, 2, 5, 2]

def test_reverse_even_elements_positive_zero_as_even():
    arr = [0, 1, 2, 3, 4]
    assert reverse_even_elements(arr) == [4, 1, 2, 3, 0]

def test_reverse_even_elements_positive_large_numbers():
    arr = [1000, 1001, 1002, 1003, 1004]
    assert reverse_even_elements(arr) == [1004, 1001, 1002, 1003, 1000]

# Негативные тесты
def test_reverse_even_elements_negative_non_list_input():
    with pytest.raises(TypeError):
        reverse_even_elements("not a list")

def test_reverse_even_elements_negative_string_elements():
    arr = [1, "two", 3, 4]
    with pytest.raises(TypeError):
        reverse_even_elements(arr)

def test_reverse_even_elements_negative_mixed_types():
    arr = [1, 2, "three", 4]
    with pytest.raises(TypeError):
        reverse_even_elements(arr)

def test_reverse_even_elements_negative_none_elements():
    arr = [1, None, 3, 4]
    with pytest.raises(TypeError):
        reverse_even_elements(arr)

def test_reverse_even_elements_negative_bool_elements():
    arr = [1, True, 3, False]
    new_arr = reverse_even_elements(arr)
    assert isinstance(new_arr, list)

# Граничные тесты
def test_reverse_even_elements_boundary_empty_list():
    arr = []
    assert reverse_even_elements(arr) == []

def test_reverse_even_elements_boundary_single_element_even():
    arr = [42]
    assert reverse_even_elements(arr) == [42]

def test_reverse_even_elements_boundary_single_element_odd():
    arr = [7]
    assert reverse_even_elements(arr) == [7]

def test_reverse_even_elements_boundary_two_elements_both_even():
    arr = [2, 4]
    assert reverse_even_elements(arr) == [4, 2]

def test_reverse_even_elements_boundary_two_elements_both_odd():
    arr = [1, 3]
    assert reverse_even_elements(arr) == [1, 3]

def test_reverse_even_elements_boundary_two_elements_mixed():
    arr = [2, 3]
    assert reverse_even_elements(arr) == [2, 3]

def test_reverse_even_elements_boundary_large_list():
    arr = list(range(1, 1001))
    new_arr = reverse_even_elements(arr)
    assert len(new_arr) == 1000
    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            assert new_arr[i] == arr[i]

def test_reverse_even_elements_boundary_evens_at_ends():
    arr = [2, 1, 3, 5, 4]
    assert reverse_even_elements(arr) == [4, 1, 3, 5, 2]

def test_reverse_even_elements_boundary_negative_k_like_conditions():
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    new_arr = reverse_even_elements(arr)
    expected = [1, 8, 3, 6, 5, 4, 7, 2]
    assert new_arr == expected


# Позитивные тесты
def test_large_integer_plus_one_positive_simple_increment():
    digits = [1, 2, 3]
    assert large_integer_plus_one(digits) == [1, 2, 4]

def test_large_integer_plus_one_positive_increment_middle_digit():
    digits = [1, 9, 9]
    assert large_integer_plus_one(digits) == [2, 0, 0]

def test_large_integer_plus_one_positive_increment_single_digit_not_nine():
    digits = [5]
    assert large_integer_plus_one(digits) == [6]

def test_large_integer_plus_one_positive_increment_with_carry_at_end():
    digits = [1, 2, 9]
    assert large_integer_plus_one(digits) == [1, 3, 0]

def test_large_integer_plus_one_positive_increment_with_multiple_carries():
    digits = [1, 9, 9, 9]
    assert large_integer_plus_one(digits) == [2, 0, 0, 0]

def test_large_integer_plus_one_positive_increment_all_nines():
    digits = [9, 9, 9]
    assert large_integer_plus_one(digits) == [1, 0, 0, 0]

def test_large_integer_plus_one_positive_increment_large_number():
    digits = [4, 3, 2, 1]
    assert large_integer_plus_one(digits) == [4, 3, 2, 2]

def test_large_integer_plus_one_positive_increment_with_zero():
    digits = [1, 0, 0, 0]
    assert large_integer_plus_one(digits) == [1, 0, 0, 1]

def test_large_integer_plus_one_positive_increment_with_carry_through_zeros():
    digits = [1, 9, 0, 9]
    assert large_integer_plus_one(digits) == [1, 9, 1, 0]

def test_large_integer_plus_one_positive_increment_single_nine():
    digits = [9]
    assert large_integer_plus_one(digits) == [1, 0]

# Негативные тесты
def test_large_integer_plus_one_negative_empty_list():
    digits = []
    result = large_integer_plus_one(digits)
    assert result == []

def test_large_integer_plus_one_negative_none_input():
    digits = None
    result = large_integer_plus_one(digits)
    assert result == []

def test_large_integer_plus_one_negative_non_list_input():
    with pytest.raises(TypeError):
        large_integer_plus_one("123")

def test_large_integer_plus_one_negative_leading_zero():
    digits = [0, 1, 2]
    result = large_integer_plus_one(digits)
    assert result == [0, 1, 3]

def test_large_integer_plus_one_negative_string_digits():
    digits = ["1", "2", "3"]
    with pytest.raises(TypeError):
        large_integer_plus_one(digits)

# Граничные тесты
def test_large_integer_plus_one_boundary_minimum_length():
    digits = [0]
    assert large_integer_plus_one(digits) == [1]

def test_large_integer_plus_one_boundary_all_zeros_except_first():
    digits = [1, 0, 0, 0, 0]
    assert large_integer_plus_one(digits) == [1, 0, 0, 0, 1]

def test_large_integer_plus_one_boundary_digit_zero_at_end():
    digits = [1, 2, 3, 0]
    assert large_integer_plus_one(digits) == [1, 2, 3, 1]

def test_large_integer_plus_one_boundary_digit_nine_at_end_with_carry():
    digits = [1, 2, 3, 9]
    assert large_integer_plus_one(digits) == [1, 2, 4, 0]

def test_large_integer_plus_one_boundary_single_digit_zero():
    digits = [0]
    assert large_integer_plus_one(digits) == [1]