import math


def division_sum(number):
    """
    вычисление кратной суммы
    """

    result = 0  # Конечный результат суммирования делителей
    i = 2
    while i <= (math.sqrt(number)):  # Поиск всех делителей, которые делят число
        if number % i == 0:  # Если i - целочисленный делитель числа
            if i == (number / i):  # если оба делителя равны, то суммируем его с результатом,
                result = result + i
            else:
                result = result + (i + number / i)  # иначе добавляем оба делителя
        i += 1
    return int(result + 1)  # увеличиваем результат на 1


def buddy(start, limit):
    for number in range(start, limit):  # проходим в заданных пределаж
        min_pair = number + 1
        aliquot_sum = division_sum(number)  # кратная сумма
        max_pair = aliquot_sum - 1
        if division_sum(max_pair) == min_pair:
            return [number, max_pair]  # искомая пара
    return 'None'  # нет искомых пар


def main():
    print(buddy(start=10, limit=50))


if __name__ == '__main__':
    main()
