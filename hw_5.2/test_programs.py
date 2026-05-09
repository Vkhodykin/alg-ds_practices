import pytest
from programs import factorial
from programs import fibonacci


# Позитивные тесты
def test_factorial_zero():
    result = factorial(0)
    assert result == 1
    assert isinstance(result, int)

def test_factorial_one():
    result = factorial(1)
    assert result == 1
    assert isinstance(result, int)

def test_factorial_two():
    result = factorial(2)
    assert result == 2

def test_factorial_three():
    result = factorial(3)
    assert result == 6

def test_factorial_four():
    result = factorial(4)
    assert result == 24

def test_factorial_five():
    result = factorial(5)
    assert result == 120

def test_factorial_six():
    result = factorial(6)
    assert result == 720

def test_factorial_seven():
    result = factorial(7)
    assert result == 5040

def test_factorial_eight():
    result = factorial(8)
    assert result == 40320

def test_factorial_nine():
    result = factorial(9)
    assert result == 362880

def test_factorial_ten():
    result = factorial(10)
    assert result == 3628800

def test_factorial_eleven():
    result = factorial(11)
    assert result == 39916800

def test_factorial_twelve():
    result = factorial(12)
    assert result == 479001600

def test_factorial_thirteen():
    result = factorial(13)
    assert result == 6227020800

def test_factorial_fourteen():
    result = factorial(14)
    assert result == 87178291200

def test_factorial_fifteen():
    result = factorial(15)
    assert result == 1307674368000

def test_factorial_sixteen():
    result = factorial(16)
    assert result == 20922789888000

def test_factorial_seventeen():
    result = factorial(17)
    assert result == 355687428096000

def test_factorial_eighteen():
    result = factorial(18)
    assert result == 6402373705728000

def test_factorial_nineteen():
    result = factorial(19)
    assert result == 121645100408832000

def test_factorial_twenty():
    result = factorial(20)
    assert result == 2432902008176640000

# Негативные тесты
def test_negative_factorial_one():
    result = factorial(-1)
    assert isinstance(result, ValueError)
    assert str(result) == ""

def test_negative_factorial_five():
    result = factorial(-5)
    assert isinstance(result, ValueError)

def test_negative_factorial_ten():
    result = factorial(-10)
    assert isinstance(result, ValueError)

def test_negative_factorial_twenty():
    result = factorial(-20)
    assert isinstance(result, ValueError)

def test_negative_factorial_twenty_one():
    result = factorial(21)
    assert isinstance(result, ValueError)

def test_negative_factorial_twenty_five():
    result = factorial(25)
    assert isinstance(result, ValueError)

def test_negative_factorial_thirty():
    result = factorial(30)
    assert isinstance(result, ValueError)

def test_negative_factorial_fifty():
    result = factorial(50)
    assert isinstance(result, ValueError)

def test_negative_factorial_hundred():
    result = factorial(100)
    assert isinstance(result, ValueError)

# Граничные тесты
def test_factorial_boundary_zero():
    result = factorial(0)
    assert result == 1
    assert isinstance(result, int)

def test_factorial_boundary_one():
    result = factorial(1)
    assert result == 1

def test_factorial_boundary_twenty():
    result = factorial(20)
    assert result == 2432902008176640000

def test_factorial_boundary_negative_one():
    result = factorial(-1)
    assert isinstance(result, ValueError)

def test_factorial_boundary_twenty_one():
    result = factorial(21)
    assert isinstance(result, ValueError)

def test_factorial_type_int_return():
    for n in range(0, 21):
        result = factorial(n)
        assert isinstance(result, int)
        assert result > 0

def test_factorial_sequence_values():
    expected = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
    for n in range(11):
        assert factorial(n) == expected[n]

def test_factorial_property():
    for n in range(1, 21):
        assert factorial(n) == n * factorial(n - 1)


# Позитивные тесты
def test_fibonacci_zero():
    result = fibonacci(0)
    assert result == [0]
    assert isinstance(result, list)
    assert len(result) == 1

def test_fibonacci_one():
    result = fibonacci(1)
    assert result == [0, 1]
    assert len(result) == 2

def test_fibonacci_two():
    result = fibonacci(2)
    assert result == [0, 1, 1]

def test_fibonacci_three():
    result = fibonacci(3)
    assert result == [0, 1, 1, 2]

def test_fibonacci_four():
    result = fibonacci(4)
    assert result == [0, 1, 1, 2, 3]

def test_fibonacci_five():
    result = fibonacci(5)
    assert result == [0, 1, 1, 2, 3, 5]

def test_fibonacci_six():
    result = fibonacci(6)
    assert result == [0, 1, 1, 2, 3, 5, 8]

def test_fibonacci_seven():
    result = fibonacci(7)
    assert result == [0, 1, 1, 2, 3, 5, 8, 13]

def test_fibonacci_eight():
    result = fibonacci(8)
    assert result == [0, 1, 1, 2, 3, 5, 8, 13, 21]

def test_fibonacci_nine():
    result = fibonacci(9)
    assert result == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

def test_fibonacci_ten():
    result = fibonacci(10)
    assert result == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

def test_fibonacci_fifteen():
    result = fibonacci(15)
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
    assert result == expected
    assert len(result) == 16

def test_fibonacci_twenty():
    result = fibonacci(20)
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610,
                987, 1597, 2584, 4181, 6765]
    assert result == expected
    assert len(result) == 21

def test_fibonacci_twenty_five():
    result = fibonacci(25)
    assert result[25] == 75025  # F(25) = 75025
    assert result[20] == 6765   # F(20) = 6765
    assert len(result) == 26

# Негативные тесты
def test_fibonacci_negative_one():
    with pytest.raises(ValueError):
        fibonacci(-1)

def test_fibonacci_negative_five():
    with pytest.raises(ValueError):
        fibonacci(-5)

def test_fibonacci_negative_ten():
    with pytest.raises(ValueError):
        fibonacci(-10)

def test_fibonacci_negative_twenty():
    with pytest.raises(ValueError):
        fibonacci(-20)

def test_fibonacci_negative_one_hundred():
    with pytest.raises(ValueError):
        fibonacci(-100)

# Граничные тесты
def test_fibonacci_boundary_zero():
    result = fibonacci(0)
    assert result == [0]
    assert isinstance(result, list)
    assert len(result) == 1

def test_fibonacci_boundary_one():
    result = fibonacci(1)
    assert result == [0, 1]
    assert len(result) == 2

def test_fibonacci_boundary_two():
    result = fibonacci(2)
    assert result == [0, 1, 1]
    assert result[1] == 1
    assert result[2] == 1

def test_fibonacci_boundary_negative_one():
    with pytest.raises(ValueError):
        fibonacci(-1)

def test_fibonacci_large_n():
    result = fibonacci(100)
    assert len(result) == 101
    assert result[100] == 354224848179261915075  # F(100)
    assert isinstance(result[100], int)

def test_fibonacci_consistency():
    n = 15
    result = fibonacci(n)
    for i in range(2, n + 1):
        assert result[i] == result[i-1] + result[i-2]

def test_fibonacci_return_type():
    result = fibonacci(10)
    assert isinstance(result, list)
    assert all(isinstance(x, int) for x in result)

def test_fibonacci_sequence_length():
    for n in range(0, 21):
        result = fibonacci(n)
        assert len(result) == n + 1

def test_fibonacci_first_two_elements():
    for n in range(1, 21):
        result = fibonacci(n)
        assert result[0] == 0
        assert result[1] == 1
