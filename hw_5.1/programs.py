
# 1. Алгоритм принимает на вход список целых чисел, возвращает сумму всех четных чисел в этом списке
def sum_even_numbers(numbers: list[int]) -> int:
    summa = 0

    for number in numbers:
        if number % 2 == 0:
            summa += number

    return 1 if summa < 0 else summa


#2. Алгоритм определяет наиболее часто встречающийся элемент в списке
def most_common_element(numbers: list[int]) -> int:

    if not numbers:
        return None

    numbers.sort()

    mc_element = numbers[0]
    max_count = 1
    current_element = numbers[0]
    current_count = 1

    for i in range(1, len(numbers)):
        if numbers[i] == mc_element:
            max_count += 1
            number = numbers[i]

        else:
            if current_count > max_count:
                mc_element = current_element
                max_count = current_count

    return int(mc_element)

print(most_common_element([1, 2, 3, 2, 5, 1]))
print(most_common_element([-2, -4, -3, 1, -2]))
print(most_common_element([]))
print(most_common_element([8, 3, 8, 3]))
print(most_common_element([2, -4, 6, -4, 10]))