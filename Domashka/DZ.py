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

# Вариант №3
# c = tuple(input("Введите по порядку без пробелов элементы кортежа: "))
# cc = tuple(sorted(c))
# print(cc)
# ii = "0"
# n = 0
# for i in cc:
#     if i == ii:
#         n = n + 1
#     if i != ii:
#         print("Количество ", ii, "=", n)  # для предыдущего элемента
#         n = 1
#     ii = i
# print("Количество ", i, "=", n)  # для последнего элемента


# ДЗ №10 от 29.01.2024
# Строка кода :)


# ДЗ №11 от 31.01.2024
# Задача:
# Олимпиада
# physics = {"Matvei", "Evgeniya", "Michail", "Maxim", "Natalia"}
# mathematics = {"Maxim", "Matvei", "Aleksandr"}
# general_list = physics | mathematics
# print("Все призеры:", general_list)
# both_olympiads = physics & mathematics
# print("Призеры обеих олимпиад:", both_olympiads)
# mathematics &= both_olympiads
# print("Обновленный список по математике:", mathematics)


# ДЗ №12 от 05.02.2024
# Задача:
# sales = {'John': {'N': 3056, 'S': 8463, 'E': 8441, 'W': 2694},
#          'Tom': {'N': 4832, 'S': 6786, 'E': 4737, 'W': 3612},
#          'Anne': {'N': 5239, 'S': 4802, 'E': 5820, 'W': 1859},
#          'Fiona': {'N': 3904, 'S': 3645, 'E': 8821, 'W': 2451}}
#
# for x in sales:
#     print(x)
#     for y in sales[x]:
#         print("\t", y, ":", sales[x][y])
#
# person = input("Имя: ")
# region = input("Регион: ")
# print(sales[person][region])
# new_data = int(input("Новое значение: "))
# sales[person][region] = new_data
# print(sales[person])


# ДЗ №13 от 07.02.2024
# Задача:
# students = {}
# n = int(input("Количество студентов: "))
# s = 0
# for i in range(n):
#     name = input(str(i + 1) + "-й студент: ")
#     points = int(input("Балл: "))
#     students[name] = points
#     s += points
#
# average = s / n
# print("Средний балл: ", average)
# for i in students:
#     if students[i] > average:
#         print(i)


# ДЗ №14 от 12.02.2024
# Задача:
# def outer(a, b, c):
#     def inner(i, j):
#         return i * j
#
#     s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
#     return s
#
#
# print(outer(2, 4, 6))
# print(outer(5, 8, 2))
# print(outer(1, 6, 8))


# ДЗ №15 от 14.02.2024
# Задача:
# Дан список слов. Отфильтровать список с использованием lambda-выражения, оставив в нем слова-палиндромы.
# Тестовые значения: ('madam', 'fire', 'tomato', 'book', 'kiosk', 'mom') -> (madam, mom)

# Разные варианты
# Вариант №1
# def f(x):
#     if x == x[::-1]:
#         return True
#     else:
#         return False
#
#
# a = ['madam', 'fire', 'tomato', 'book', 'kiosk', 'mom']
# b = list(filter(f, a))
# print(b)


# Вариант №2
# def f(x):
#     return x == x[::-1]
#
#
# a = ['madam', 'fire', 'tomato', 'book', 'kiosk', 'mom']
# b = list(filter(f, a))
# print(b)


# Вариант №3
# a = ['madam', 'fire', 'tomato', 'book', 'kiosk', 'mom']
# b = list(filter(lambda x: x == x[::-1], a))
# print(b)

# Стоки нельзя изменить, но можно перезаписать в другую переменную с новыми значениями!


# ДЗ №16 от 19.02.2024
# Задача:
# Создать функцию, которая будет находить сумму любого количества чисел. И декоратор,
# который будет находить среднее арифметическое этих чисел
# def avg(fn):
#     def wrap(*arg):
#         print("Среднее арифметическое: ", *arg, "=", fn(*arg) / len(arg))
#
#     return wrap
#
#
# @avg
# def summa(*args):
#     print("Сумма чисел: ", *args, "=", sum(args))
#     return sum(args)
#
#
# summa(2, 3, 3, 4)


# ДЗ №17 от 21.02.2024
# Задача:
# Пользователь вводит ФИО. Приложение выводит фамилию и инициалы.
# fio = input("Введите ФИО: ").split()
# print(fio)
# print(f"{fio[0]} {fio[1][0]}. {fio[2][0]}.")

import re


# ДЗ №18 от 26.02.2024
# Задача:
# Найти номер телефона в формате +7хххххххххх или 7хххххххххх

# s = "+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 74994564578, +24994564578"
# reg = r"\+?7\d{10}"  # \d - только цифры, {10} - сколько цифр
# print(re.findall(reg, s))


# ДЗ №19 от 28.02.2024
# Задача:
# Проверка соответствия пароля. Он должен состоять из цифр, букв английского алфавита, дефис, собака и
# подчеркивание. Длина пароля от 6 до 18 символов.

# import re
#
# s = "my-p@ssword, rdjjk_1, 123798@, 7 (499) 456 45 78, *nhgk*, urttrryuuyuyyyurtrrtrtr-trrr"
# reg = r"[a-zA-Z0-9\_\-\@]{6,18}"
# print(re.findall(reg, s))


# while True:
#     password = input('Input a strong password: ')
#     if re.match(r'[A-Za-z0-9@#$%^&+=]{8,16}', password):
#         print('Very nice password. Much secure')
#         break
#     else:
#         print('Not a valid password')


# ДЗ №20 от 04.03.2024
# Задача:
# Вычислить количество отрицательных чисел в массиве с помощью рекурсии:

# def negative_numbers(n):
#     if not n:
#         return 0
#     count = 0
#     if n[0] < 0:
#         count += 1
#     return count + negative_numbers(n[1:])
#
#
# lst = [-2, 3, 8, -11, -4, 6]
# print(negative_numbers(lst))


# ДЗ №21 от 06.03.2024
# Задача:
# Выведите на экран сначала все файлы, а затем все директории, расположенные в корневой директории дерева.
# ['files\\one.txt', 'files\\three.txt', 'files\\two.txt', 'files\\dir']
# import os
# import os.path
#
# for root, dirs, files in os.walk("../nested1", topdown=False):
#     a = os.listdir(root)
#     print(a)


# root = r"nested1\nested2"
# objs = os.listdir(root)
# print(objs)
# print(sorted(os.listdir("Work"), reverse=True))


# ДЗ №22 от 11.03.2024
# Задача:
# Реализуйте класс "Автомобиль"
# Вариант №1
# class Auto:
#     model = "series number"
#     year = "0000"
#     manufacturer = "name"
#     power = "000 h.p."
#     color = "color"
#     price = "00000000"
#
#     def print_info(self):
#         print(" Данные автомобиля ".center(40, "*"))
#         print(f"Название модели: {self.model}\nГод выпуска: {self.year}\nПроизводитель: {self.manufacturer}\n"
#               f"Мощность двигателя: {self.power}\nЦвет машины: {self.color}\nЦена: {self.price}")
#         print("=" * 40)
#
#     def input_info(self, model, year, manufacturer, power, color, price):
#         self.model = model
#         self.year = year
#         self.manufacturer = manufacturer
#         self.power = power
#         self.color = color
#         self.price = price
#
#     def set_manufacturer(self, manufacturer):  # меняем производителя
#         self.manufacturer = manufacturer
#
#     def get_manufacturer(self):
#         return self.manufacturer
#
#
# a1 = Auto()
# a1.print_info()
# a1.input_info("X7 M50i", "2021", "BMW", "530 л.с.", "white", "10790000")
# a1.print_info()
# a1.set_manufacturer("Mercedes")
# a1.print_info()
# print((a1.get_manufacturer()))


# Вариант №2
# class Auto:
#
#     def __init__(self, model, year, manufacturer, power, color, price):
#         self.model = model
#         self.year = year
#         self.manufacturer = manufacturer
#         self.power = power
#         self.color = color
#         self.price = price
#
#     def print_info(self):
#         print(" Данные автомобиля ".center(40, "*"))
#         print(f"Название модели: {self.model}\nГод выпуска: {self.year}\nПроизводитель: {self.manufacturer}\n"
#               f"Мощность двигателя: {self.power}\nЦвет машины: {self.color}\nЦена: {self.price}")
#         print("=" * 40)
#
#     def set_model(self, model):
#         self.model = model
#
#     def set_year(self, year):
#         self.year = year
#
#     def set_manufacturer(self, manufacturer):
#         self.manufacturer = manufacturer
#
#     def set_power(self, power):
#         self.power = power
#
#     def set_color(self, color):
#         self.color = color
#
#     def set_price(self, price):
#         self.price = price
#
#     def get_model(self):
#         return self.model
#
#     def get_manufacturer(self):
#         return self.manufacturer
#
#
# a1 = Auto("X7 M50i", "2021", "BMW", "530 л.с.", "white", "10790000")
# a1.print_info()
#
# # сеттеры
# a1.set_model("benz c-class")
# a1.set_year("2024")
# a1.set_manufacturer("Mercedes")
# a1.set_power("204 л.с.")
# a1.set_color("red")
# a1.set_price("142.000$")
# a1.print_info()
#
# # геттеры
# print((a1.get_model()))
# print((a1.get_manufacturer()))


# ДЗ №23 от 13.03.2024
# Задача:
# Создать класс Person c двумя закрытыми свойствами в Python: имя и возраст. С использованием декоратора @property
# создать возможность изменения и удаления этих свойств.

# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     @property  # Функция property() возвращает атрибут свойства из заданного геттера, сеттера и делитера.
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, new_name):
#         self.__name = new_name
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, new_age):
#         self.__age = new_age
#
#     @age.deleter
#     def age(self):
#         del self.__age
#
#
# person = Person("Виктор", 30)
# print(person.name)  # Вывод: Виктор
# print(person.age)  # Вывод: 30
# print(person.__dict__)  # {'_Person__name': 'Виктор', '_Person__age': 30}
#
# person.name = "Елена"
# person.age = 25
#
# print(person.name)  # Вывод: Елена
# print(person.age)  # Вывод: 25
# print(person.__dict__)  # {'_Person__name': 'Елена', '_Person__age': 25}
#
# del person.name
# # print(person.name)  # Будет вызвано исключение AttributeError
# print(person.__dict__)  # {'_Person__age': 25}
#
# del person.age
# # print(person.age)   # Будет вызвано исключение AttributeError


# ДЗ №24 от 18.03.2024
# Задача:
# Создайте класс для подсчета площади геометрических фигур в Python. Класс должен предоставлять
# функциональность для подсчета площади треугольника по разным формулам (площадь треугольника по формуле Герона,
# площадь треугольника через основание и высоту), площади прямоугольника, площади квадрата. Методы класса
# для подсчета площади должны быть реализованы с помощью статических методов. Также класс должен считать
# количество подсчетов площади и возвращать это значение с помощью статического метода.

class Point:
    __count = 0  # Статическая переменная для отслеживания количества подсчетов

    @staticmethod
    def triangle_heron(a, b, c):
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        Point.__count += 1
        return area

    @staticmethod
    def triangle_base_height(base, height):
        area = 0.5 * base * height
        Point.__count += 1
        return area

    @staticmethod
    def square(side):
        area = side * side
        Point.__count += 1
        return area

    @staticmethod
    def rectangle(width, height):
        area = width * height
        Point.__count += 1
        return area

    @staticmethod
    def get_count():  # get_count() позволяет получить общее количество подсчетов площади
        return Point.__count


print("Площадь треугольника по формуле Герона:", Point.triangle_heron(3, 4, 5))
print("Площадь треугольника через основание и высоту:", Point.triangle_base_height(6, 7))
print("Площадь квадрата:", Point.square(7))
print("Площадь прямоугольника:", Point.rectangle(2, 6))

# Получение количества подсчетов
print("Количество подсчетов площади:", Point.get_count())  # Ожидаемое значение: 4
