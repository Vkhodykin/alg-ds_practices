import pytest
from programs import max_in_range
from programs import rotate_and_reverse

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
