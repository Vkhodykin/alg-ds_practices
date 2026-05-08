
# 1. Алгоритм принимает на вход список целых чисел, возвращает сумму всех четных чисел в этом списке
def sum_even_numbers(numbers: list[int]) -> int:
    summa = 0

    for number in numbers:
        if number % 2 == 0:
            summa += number

    return 1 if summa < 0 else summa

# O(n) = 1 + n * (1 + 1 + 1 + 1 + 1) = 1 + 5 * n = 5 * n = n -> O(n)


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
        if numbers[i] == current_element:
            current_count += 1

        else:
            # Проверка текущего элемента на самый частый
            if current_count > max_count:
                mc_element = current_element
                max_count = current_count
            # Начинаем подсчет для нового элемента
            current_element = numbers[i]
            current_count = 1

    # Проверяем последний элемент
    if current_count > max_count:
        mc_element = current_element
        max_count = current_count

    elif current_count == max_count and current_element < mc_element:
        mc_element = current_element

    return int(mc_element)

# O(n) = 1 + 1 + 1 + 1 + 1 + n * (1 + 1 + 1 + 1) + n * (1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1)
#       + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 = 5 + n * 4 + n * 10 + 11 = n * 4 + n * 10 = n + n = n -> O(n)


# 3. Алгоритм находит индексы, сумма которых равна заданному значению
def sum_two_indexes(numbers: list[int], target: int) -> list[int] | None:

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:

                return [i, j]

    return None

# O(n) = n * (n * (1 + 1 + 1 + 1 + 1) = n * (n * 5) = n**2 * 5 * n = n**2 * n = O(n**k)
