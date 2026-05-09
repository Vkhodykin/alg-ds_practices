import pytest
from programs import factorial



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