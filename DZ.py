import random
import math

# ДЗ №1 от 18.12.2023
# Обмен значениями переменных арифметический способ
# Третий способ:
# a = 19
# b = 205
# print("a:", a)
# print("b:", b)
# a = a + b # 19 + 205 = 224
# b = a - b # 224 - 205 = 19
# a = a - b # 224 - 19 = 205
# print("a:", a)
# print("b:", b)

# nam = input("Who are you?")
# print("Welcome", nam)


# ДЗ №2 от 20.12.2023
# Написать слово "КОПЕЕК" в правильном формате (диапазон от 1 до 99)
# 1 Вариант:
# money = int(input("Введите число копеек от 1 до 99: "))
# if 1 <= money <= 99:
#     print("Вы ввели:", end=" ")
#     if money == 1 or money == 21 or money == 31 or money == 41 or money == 51\
#             or money == 61 or money == 71 or money == 81 or money == 91:
#         print(money, "копейка")
#     elif 2 <= money <= 4 or 22 <= money <= 24 or 32 <= money <= 34 or 42 <= money <= 44 or \
#             52 <= money <= 54 or 62 <= money <= 64 or 72 <= money <= 74 or \
#             82 <= money <= 84 or 92 <= money <= 94:
#         print(money, "копейки")
#     else:
#         print(money, "копеек")
# else:
#     print("Ошибка ввода данных")


# 2 Вариант:
# money = int(input("Введите число копеек от 1 до 99: "))
# if 1 <= money <= 99:
#     print("Вы ввели:", end=" ")
#     if money % 10 == 1 and money % 100 != 11:
#         print(money, "копейка")
#     elif money % 10 in [2, 3, 4] and money % 100 not in [12, 13, 14]:
#         print(money, "копейки")
#     else:
#         print(money, "копеек")
# else:
#     print("Ошибка ввода данных")


# ДЗ №3 от 25.12.2023
# Задача:
# Написать программу, которая выводит на экран линию из символов. Пользователь сам указывает:
# число символов, тип символа, и ориентацию линии - вертикальную или горизонтальную
# n = int(input("Укажите количество символов: "))
# m = input("Укажите тип символов: ")
# l = int(input("Укажите ориентацию линии: 0 - горизонтальная, 1 - вертикальная: "))
# print("Количество -", n)
# print("Тип вашего символа -", m)
# print("Ориентация линии -", l)
# if l == 0:
#     print("Результат: ", (n * m))
# else:
#     print("Результат: ", (("\n" + m) * n))


# ДЗ №4 от 27.12.2023
# Написать программу, которая вычисляет среднее - арифметическое последовательности дробных чисел.
# После ввода последнего числа программа должны вывести минимальное и максимальное число последовательности.
# Количество чисел последовательности должно задаваться во время работы программы.
# a = [float(input("Введите число: ")) for i in range(int(input("Введите количество чисел последовательности: ")))]
# print("Количество чисел:", len(a))
# print("Среднее - арифметическое: ", round(sum(a) / len(a), 1))
# print("Минимальное число:", min(a))
# print("Максимальное число:", max(a))


# ДЗ №5 от 10.01.2024
# Программа должна просить пользователя заданное количество раз ввести число, кратное 3,
# проверять, действительно ли оно кратно 3. если да, то добавлять в список, если нет, то выводить
# пользователю на экране *введенное пользователем число* не делится на 3 без остатка.
# s = []
# n = int(input("Введите количество элементов списка: "))
# for i in range(n):
#     a = int(input("Введите число, кратное 3-м: "))
#     if a % 3 == 0:
#         s.append(a)
#     else:
#         print(a, "не делится на 3 без остатка.")
# print(s)


# ДЗ №6 от 15.01.2024
# Дан список целых чисел, число k (индекс) и значение С. Необходимо вставить в список на позицию
# с индексом k элемент, равный С, сдвинув все элементы, имевшие индекс не менее k, вправо.
# sp = [int(input("-> ")) for i in range(int(input("Введите количество чисел списка: ")))]
# print(sp)
# a = int(input("Введите индекс: "))
# print(a)
# b = int(input("Введите значение: "))
# print(b)
# sp.insert(a, b)
# print(sp)


import math
from math import sqrt
from math import pi

# ДЗ №7 от 17.01.2024
# Вычисление площади фигур. Выбор фигуры:
# 1. треугольник
# 2. прямоугольник
# 3. круг
# : 1 Введите сторону a = 15 Введите сторону b = 20 Введите сторону c = 6 Итого - 28.59
# ---------------------------------------------------------------------------------------
# Решение:
# figure = int(input("Выберите фигуру из списка, чтобы посчитать ее площадь (1 - треугольник\
#  2 - прямоугольник 3 - Круг): "))
# if figure == 1:
#     print("Ваша фигура - треугольник")
#     a = int(input("Введите сторону a: "))
#     b = int(input("Введите сторону b: "))
#     c = int(input("Введите сторону c: "))
#     p = (a + b + c) / 2
#     print("Площадь треугольника - ", round(sqrt(p * (p - a) * (p - b) * (p - c)), 2))
# elif figure == 2:
#     print("Ваша фигура - прямоугольник")
#     a = int(input("Введите сторону a: "))
#     b = int(input("Введите сторону b: "))
#     print("Площадь прямоугольника - ", a * b)
# elif figure == 3:
#     print("Ваша фигура - круг")
#     radius = int(input("Введите радиус: "))
#     print("Площадь круга - ", round(pi * radius ** 2, 2))
# else:
#     print("Такой фигуры не существует")


# ДЗ №8 от 22.01.2024
# Делать на основе функций

# def triangle():
#     a = int(input("Введите основание: "))
#     b = int(input("Введите высоту: "))
#     return (a * b) / 2
#
#
# def rectangle():
#     a = int(input("Введите сторону a: "))
#     b = int(input("Введите сторону b: "))
#     return a * b
#
#
# def circle():
#     radius = int(input("Введите радиус: "))
#     return round(pi * radius ** 2, 2)
#
#
# figure = int(input("Выберите фигуру из списка: \n1 - треугольник \n2 - прямоугольник \n3 - Круг \n: "))
# if figure == 1:
#     print(triangle())
# elif figure == 2:
#     print(rectangle())
# elif figure == 3:
#     print(circle())
# else:
#     print("Такой фигуры не существует")


# ДЗ №9 от 24.01.2024
# Введите статистику частотности символов в кортеже
# Вариант №1
# a = input("Введите по порядку без пробелов элементы кортежа: ")
# print(tuple(a))
# for i in set(a):
#     print("Количество ", i, "=", a.count(i))


# Вариант №2
# a = input("Введите по порядку без пробелов элементы кортежа: ")
# print(tuple(a))
# b = []
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)
# for i in b:
#     print("Количество ", i, "=", a.count(i))


# ДЗ №10 от 29.01.2024

# Вариант №3
c = tuple(input("Введите по порядку без пробелов элементы кортежа: "))
cc = tuple(sorted(c))
print(cc)
ii = "0"
n = 0
for i in cc:
    if i == ii:
        n = n + 1
    if i != ii:
        print("Количество ", ii, "=", n)  # для предыдущего элемента
        n = 1
    ii = i
print("Количество ", i, "=", n)  # для последнего элемента







