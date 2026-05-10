
# Задача №1
def max_in_range(arr: list[int], start: int, end: int) -> tuple[int, int, int]:
    if not arr:
        raise ValueError("Массив не может быть пустым")
    if start < 0 or end >= len(arr) or start > end:
        raise ValueError("Некорректные значения start и end")

    maxima = arr[start]
    absolute_index = start

    for i in range(start, end + 1):
        if arr[i] > maxima:
            maxima = arr[i]
            absolute_index = i

    relative_index = absolute_index - start

    return maxima, absolute_index, relative_index

# O(n) = 1 + 1 + n * (1 + 1 + 1 + 1 + 1) + 1 + 1 + 1 = 2 + n * 5 + 3 = 5 + n * 5 = n * 5 = n -> O(n)


# Задача №2
def rotate_and_reverse(arr: list[int], k: int) -> list[int]:
    if not arr:
        return []

    k = k % len(arr)   # нормализуем k на случай, если оно больше длины списка

    if k > 0:
        cyclic_shift = arr[-k:] + arr[:-k]  # циклический сдвиг вправо, берем последние k-элементы и переносим в начало, остальные элементы сдвигаются
    else:
        cyclic_shift = arr[:] # список копируется

    reversed_result = cyclic_shift[::-1]    # инверсия всего списка

    return reversed_result

# O(n) = 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 = 12 -> O(1)


# Задача №3
def reverse_even_elements(arr: list[int]) -> list[int]:
    if not arr:
        return []

    even_elements = []

    for element in arr:
        if element % 2 == 0:  # Находим все четные элементы
            even_elements.append(element)

    reversed_even_elements = even_elements[::-1] # Разворачиваем четные элементы

    new_arr = []
    even_elements_index = 0

    for element in arr:
        if element % 2 == 0:
            new_arr.append(reversed_even_elements[even_elements_index]) # Добавляем следующий четный элемент из развернутого списка
            even_elements_index += 1
        else:
            new_arr.append(element) # Оставляем нечетный элемент на месте

    return new_arr

# O(n) = n * (1 + 1 + 1 + 1) + 1 + 1 + 1 + n * (1 + 1 + 1 + 1 + 1 + 1 + 1) = n * 4 + 3 + n * 7 = n * 4 + n * 7 =
#      = n -> O(n)
