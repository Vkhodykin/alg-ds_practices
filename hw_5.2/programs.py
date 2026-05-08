
# Задача №1
def factorial(n: int) -> int:

    if n < 0 or n > 20:
        return ValueError()

    result = 1

    for i in range(2, n + 1):
        result *= i

    return result

# O(n) = 1 + n * (1 + 1 + 1) = 1 + n * 3 = n * 3 = n -> O(n)