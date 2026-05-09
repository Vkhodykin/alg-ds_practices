from typing import Any


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

# O(n) = 1 + 1 + n * (1 + 1 + 1 + 1 + 1 + 1 + 1) = 2 + n * 7 = n * 7 = n -> O(n)


# Задача №5
# Problem:
# Разработать алгоритм для анализа ежедневных данных о посещаемости сайта, какие дни недели, месяцы наиболее посещаемы,
# какие дни недели, месяцы наименее посещаемы.
#
# Output data:
# кортеж состоящий из:
# - список дней с наибольшей посещаемостью popular_days и наименьшей посещаемостью minima_days;
# - список месяцев с наибольшей посещаемостью popular_month и наименьшей посещаемостью minima_month;
# - список дней weekdays со средним количеством посетителей weekday_avg;
# - список месяцев months со средним количеством посетителей month_avg.
#
# Input data:
# массив данных с датами в формате YYYY-MM-DD и количеством посетителей (("2023-01-01", 150), ("2023-01-02", 200)...)
#
# Constrains:
# Ограничение на память: 256MB
# Ограничение на скорость: 2 секунды
# Максимальное количество элементов в массиве: 105

from datetime import datetime

def analyze_visitors(input_data: list[tuple[str, int] | Any]) -> tuple:

    weekday_counts = [0] * 7  # количество записей по дням недели
    weekday_sums = [0] * 7  # сумма посетителей по дням недели
    month_counts = [0] * 13  # количество записей по месяцам (индекс 0 не используется)
    month_sums = [0] * 13  # сумма посетителей по месяцам

    weekdays = ["Понедельник", "Вторник", "Среда", "Четверг",
                "Пятница", "Суббота", "Воскресенье"]
    months = ["", "Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
              "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]

    # Сбор и агрегация данных
    for date_str, visitors in input_data:
        date = datetime.strptime(date_str, "%Y-%m-%d")
        weekday = date.weekday()
        month = date.month

        weekday_counts[weekday] += 1
        weekday_sums[weekday] += visitors
        month_counts[month] += 1
        month_sums[month] += visitors

    # Расчет средних
    weekday_avg = [weekday_sums[i] / weekday_counts[i] if weekday_counts[i] > 0 else 0
                   for i in range(7)]
    month_avg = [month_sums[i] / month_counts[i] if month_counts[i] > 0 else 0
                 for i in range(13)]

    # Поиск максимумов и минимумов
    max_weekday = max(weekday_avg)
    min_weekday = min(avg for avg in weekday_avg if avg > 0)
    max_month = max(month_avg[1:])
    min_month = min(avg for avg in month_avg[1:] if avg > 0)

    # Формирование списков
    popular_days = [weekdays[i] for i, avg in enumerate(weekday_avg) if avg == max_weekday]
    minima_days = [weekdays[i] for i, avg in enumerate(weekday_avg) if avg == min_weekday]
    popular_months = [months[i] for i, avg in enumerate(month_avg) if avg == max_month]
    minima_months = [months[i] for i, avg in enumerate(month_avg) if avg == min_month]

    return (popular_days, minima_days, popular_months, minima_months,
            weekdays, weekday_avg, months[1:], month_avg)

# O(n) = 1 + 1 + 1 + 1 + 1 + 1 + n * (1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1) + n * (1 + 1 + 1) + n * (1 + 1 + 1) +
#      + 1 + n * (1) + 1 + n * (1) + n * (1 + 1) + n * (1 + 1) + n * (1 + 1) + n * (1 + 1) =
#      = 6 + n * 11 + n * 3 + n * 3 + 1 + n + 1 + n + n * 2 + n * 2 + n * 2 + n * 2 =
#      = n * 11 + n * 3 + n * 3 + n + n + n * 2 + n + 2 + n * 2 + n * 2 = n * 27 = n -> O(n)