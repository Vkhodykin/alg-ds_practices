
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

