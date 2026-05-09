
# Задача №1
def factorial(n: int) -> int:

    if n < 0 or n > 20:
        return ValueError()

    result = 1

    for i in range(2, n + 1):
        result *= i

    return result

# O(n) = 1 + n * (1 + 1 + 1) = 1 + n * 3 = n * 3 = n -> O(n)


# Задача №2
def fibonacci(n: int) -> list[int]:
    if n < 0:
        raise ValueError()
    if n == 0:
        return [0]

    list_fibonacci = [0, 1]

    for i in range(2, n + 1):
        next_value = list_fibonacci[i - 1] + list_fibonacci[i - 2]
        list_fibonacci.append(next_value)

    return list_fibonacci

# O(n) = 1 + n * (1 + 1 + 1 + 1 + 1) = 1 + n * 5 = n * 5 = n -> O(n)


# Задача №3
def count_ones(n: int) -> int:
    if n < 0:
        raise ValueError()
    if n == 0:
        return 0

    count = 0

    while n > 0:
         count += n & 1
         n >>= 1

    return count

# O(n) = 1 + n * (1 + 1 + 1) = 1 + n * 3 = n * 3 = n -> O(n)


# Задача №4
def is_palindrome(x: int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    if x < 10:
        return True

    reversed_number = 0
    number = x

    while number > 0:
        last_digit = number % 10
        reversed_number = reversed_number * 10 + last_digit
        number //= 10

    return x == reversed_number
