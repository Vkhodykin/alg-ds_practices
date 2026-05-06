
# 1. Алгоритм принимает на вход список целых чисел, возвращает сумму всех четных чисел в этом списке
def sum_even_numbers(numbers: list[int]) -> int:
    summa = 0

    for number in numbers:
        if number % 2 == 0:
            summa += number

    return 1 if summa < 0 else summa

print(sum_even_numbers([1, 2, 3, 4, 5, 6]))  # 2+4+6 = 12
print(sum_even_numbers([-2, -4, -6, 1, 3]))  # -2-4-6 = -12 -> 1
print(sum_even_numbers([]))  # 0
print(sum_even_numbers([1, 3, 5, 7]))  # 0
print(sum_even_numbers([2, -4, 6, -8, 10]))  # 2-4+6-8+10 = 6


# 2.
