import random

PI = 3.141592653589793


def test_greeting():
    """
    Напишите программу, которая выводит на экран приветствие.
    """
    name = "Анна"
    age = 25
    # TODO Сформируйте нужную строку
    output = f"Привет, {name}! Тебе {age} лет."
    # Проверяем результат
    assert output == "Привет, Анна! Тебе 25 лет."


def test_rectangle():
    """
    Напишите программу, которая берет длину и ширину прямоугольника
    и считает его периметр и площадь.
    """
    a = 10
    b = 20

    # TODO сосчитайте периметр
    perimeter = (a + b) * 2
    assert perimeter == 60

    # TODO сосчитайте площадь
    area = a * b
    assert area == 200


def test_circle():
    """
    Напишите программу, которая берет радиус круга и выводит на экран его длину и площадь.
    Используйте константу PI
    """
    r = 23
    # TODO сосчитайте площадь
    area = PI * r ** 2
    assert area == 1661.9025137490005

    # TODO сосчитайте длину окружности
    length = 2 * PI * r
    assert length == 144.51326206513048


def test_random_list():
    """
    Создайте список из 10 случайных чисел от 1 до 100 и отсортируйте его по возрастанию.
    """

    # TODO создайте список
    test_list = [random.randint(1, 100) for _ in range(10)]
    test_list.sort()
    assert len(test_list) == 10
    assert test_list[0] < test_list[-1]


def test_unique_elements():
    """
    Удалите из списка все повторяющиеся элементы
    """
    test_list = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10]
    # TODO удалите повторяющиеся элементы
    test_list = list(set(test_list))

    assert isinstance(test_list, list)
    assert len(test_list) == 10
    assert test_list == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_dicts():
    """
    Создайте словарь из двух списков.
    Используйте первый список как ключи, а второй - как значения.
    Выведите на экран все значения словаря.
    Подсказка: используй встроенную функцию zip.
    """
    first = ["a", "b", "c", "d", "e"]
    second = [1, 2, 3, 4, 5]
    # TODO создайте словарь
    d = {k: v for k, v in zip(first, second)}

    assert isinstance(d, dict)
    assert len(d) == 5
