# import random
# import math

# mas = [random.randint(0, 100) for i in range(10)]
# print(sum(mas))
# s = 0
# for i in mas:
#     s += i  # s = s + i  # s = 0 + "a"
# print(s)


# ------------------------------------------------------------------
# УРОК № 1
# ФУНКЦИИ В ПИТОН
# Функции - это многократно используемые фрагменты программы. При помощи функций можно объединить
# несколько инструкций внутри одного блока, присвоить ему имя и затем по имени, обращаясь к нему, вызывать
# функцию в любом месте необходимое число раз.


# Определение функции!
# def sayHello():
#     print('hello')
#     print('world')
#     print('and everybody')
#
#
# sayHello()


# Здесь примем 1 аргумент:
# def square(x):
#     print('Квадрат числа ', x, '=', x ** 2)
#
#
# # square(5)
# # square(10)
# # square(55)
# for i in range(1, 11):  # можем задать диапазон чисел
#     square(i)


# Примем 2 аргумента:
# def multiply(a, b):
# #     print(a * b)
# #
# #
# # multiply(3,5)
# # multiply(70, 100)


# Условия внутри функции:
# def even(a):
#     if a % 2 == 0:
#         print(a, "четное")
#     else:
#         print(a, "нечетное")
#
#
# for i in range(20, 31):
#     even(i)


# Циклы внутри функции:
# def factorial(n):
#     pr = 1
#     for i in range(2, n+1):
#         pr = pr * i
#     print(pr)
#
#
# factorial(5)


# ------------------------------------------------------------------
# УРОК № 2
# import turtle
#
#
# def move(a):
#     turtle.forward(a)
#     turtle.left(90)
#
#
# def draw_square(a):
#     for i in range(4):
#         move(a)
#
#
# def draw_square_color(a, color):
#     turtle.color(color)
#     turtle.begin_fill()
#     for i in range(4):  # draw_square(a)
#         move(a)
#     turtle.end_fill()
#
#
# turtle.speed(1)
# draw_square_color(60, 'red')
# turtle.goto(150, 150)
# draw_square_color(120, 'blue')


# ------------------------------------------------------------------
# УРОК № 3
# Функция abs возвращает модуль числа
# a = abs(-7)
# print(a)
# Встроенная функция max возвращает самое большое значение
# b = max(4, 5, abs(-90), 7, 4, 3, min(100, 200), 2)  # вначале, берутся значения в скобочках
# print(a)
# print(b)  # 100


# Любая функция в питоне возвращает какое-либо значение с помощью команды return, но если return не указан,
# то функция будет возвращать значение None
# def square(x):
#     print(x ** 2)
#     return None
#
# a = square(6)  # None
# print(a)


# def square(x):
#     return x ** 2
#
#
# a = square(6)  # 36
# print(a)


# Добавим вложенное значение функции
# def square(x):
#     return x ** 2
#
#
# a = square(square(3))  # 81 - то есть вначале находим 9, потом возводим ее во 2-ую степень
# print(a)


# def example():
#     print(1)
#     print(2)
#     return 'hello'
#     print(3)  # this code is unreachable, потому что return - выход из функции
#     print(4)
#
#
# example()


# def even(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False
#
#
# for i in range(1, 11):
#     print(i, "-", even(i))


# Здесь можно записать и без else:
# def even(x):
#     if x % 2 == 0:
#         return True
#     return False
#
#
# for i in range(1, 11):
#     print(i, "-", even(i))


# Найдем факториал:
# Эта функция должна найти произведение всех целых чисел от 1 до этого числа, включительно.
# def factorial(x):
#     pr = 1
#     for i in range(1, x + 1):
#         pr = pr * i
#     return pr
#
#
# def sochet(n, k):
#     return factorial(n) / (factorial(k) * factorial(n - k))
#
#
# print(sochet(5, 3))  # 10.0
#
# for i in range(1, 8):
#     print(i, factorial(i))


# Новая задачка:
# def sq_and_per(a, b):
#     return a * b, 2 * (a + b)
#
#
# print(sq_and_per(3, 6), type(sq_and_per(3, 6)))  # (18, 18) - результат вернулся в виде кортежа
# # (18, 18) <class 'tuple'>


# Можем использовать множественное присваивание
# def sq_and_per(a, b):
#     return a * b, 2 * (a + b)
#
#
# square, perimetr = sq_and_per(2, 5)  # 10 14
# print(square, perimetr)


# Функция можем возвращать и список:
# def sq_and_per(a, b):
#     mas = []
#     mas.append(a * b)
#     mas.append(2 * (a + b))
#     return mas
#
#
# print(sq_and_per(2, 6))  # [12, 16]


# ------------------------------------------------------------------
# УРОК № 4

# БУЛЕВО
# КОЛЛЕКЦИЯ ДАННЫХ - КОРТЕЖИ
# Кортеж - это упорядоченная, но неизменяемая коллекция произвольных данных.

# СОЗДАНИЕ КОРТЕЖА
# a = (1, 2, 3, 4, 5)
# print(a, type(a))  # (1, 2, 3, 4, 5) <class 'tuple'>
# a = 1, 2, 3, 4, 5
# print(a, type(a))  # (1, 2, 3, 4, 5) <class 'tuple'>
# a = 1,  # Запятая уже превращает наше число в кортеж - (1,) <class 'tuple'>
# print(a, type(a))

# Можно создать кортеж и с помощью одноименной функции tuple,
# там необходимо передать итерабельную последовательность, например, range()
# b = tuple(range(5))
# print(b, type(b))  # (0, 1, 2, 3, 4) <class 'tuple'>

# Также итерабельной последовательностью у нас является Список []
# b = tuple([1, 2, 3])
# print(b, type(b))  # (1, 2, 3) <class 'tuple'>

# Итерабельной последовательностью является и сам Кортеж()
# b = tuple((1, 2, 3))
# print(b, type(b))  # (1, 2, 3) <class 'tuple'>

# c = ()
# print(c, type(c))  # () <class 'tuple'>
# d = tuple()
# print(d, type(d))  # () <class 'tuple'>


# КАКИЕ ОПЕРАЦИИ ПОДДЕРЖИВАЕТ КОРТЕЖ:
# 1/ Найти длину объекта
# a = (1, 2, 3, 4, 5)
# print(len(a))  # 5
# b = tuple((4, 5))
# c = ()
# print(len(c))  # 0
# 2/ С помощью оператора in проверять наличие элемента в кортеже
# print(2 in a, 6 in a)  # True False
# print(7 not in a)  # True
# 3/ Кортежи можно складывать (сцеплять)
# print(a + b)  # (1, 2, 3, 4, 5, 4, 5)
# print(b + a)  # (4, 5, 1, 2, 3, 4, 5)
# print(a + b, b + a)  # (1, 2, 3, 4, 5, 4, 5) (4, 5, 1, 2, 3, 4, 5)
# 4/ Кортежи можно дублировать
# print(a * 2)  # (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
# 5/ Найти min и max
# print(min(a), max(a))
# # 6/ Суммировать
# print(sum(a))  # 15

# a = 1, "hello", 3, 54, False, 5
# print(a[1])  # hello
# print(a[4])  # False

# Кортеж - неизменяемая коллекция
# Сейчас появится ошибка
# a[1] = 100  # TypeError: 'tuple' object does not support item assignment
# print(a[4])

# В связи с неизменяемостью, у кортежей очень мало методов, всего 2
# a.index() - указываем Значение, которое нам нужно и если оно ув кортеже есть, index - возвращает его индекс!
# (то есть по этому методу мы ищем элемент, есть он или нет)
# a.count() - подсчитывает, сколько раз этот элемент у нас встречается

# print(a.index(6))  # цифры 6 у нас нет в кортеже, поэтому получаем ошибку
# print(a.index(4))  # цифры 4 у нас тоже нет в кортеже, ValueError: tuple.index(x): x not in tuple

# print(a.count(6))  # 0 - цифра 6 ни разу у нас не встречалась в кортеже
# print(a.count(3))  # 1 - встречалась

# В кортеже может находиться список
# a = 1, "hello", 3, [10, 20, 30], False, 5
# print(a[3])  # можно обратиться к этому вложенному списку по индексу и изменить его (список изменяем)
# a[3].append(100)
# print(a)  # (1, 'hello', 3, [10, 20, 30, 100], False, 5)


# ДЛЯ ЧЕГО НУЖНЫ КОРТЕЖИ
# 1) Неизменяемость
# a = [1, "hello", 3, [10, 20, 30], False, 5]
# b = a  # здесь мы записали в b копию переменной a
# print(a)
# print(b)
# b[2] = 100  # Если изменить элемент списка b по индексу, то также изменится и список a
# print(a)
# print(b)
# 2) Кортежи занимают меньше места в памяти
# a = [1, "hello", 3, [10, 20, 30], False, 5]
# b = tuple([1, "hello", 3, [10, 20, 30], False, 5])
# print(a.__sizeof__())  # 88
# print(b.__sizeof__())  # 72
# 2) Кортежи можно использовать в качестве ключей словаря
# a = (1, 2, 3)
# b = {}
# b[a] = 'hello'
# print(b)  # {(1, 2, 3): 'hello'}
# Если здесь использовать список, то выдаст ошибку


# Можно менять типы данных, если есть потребность изменить элементы внутри кортежа
# a = (1, 2, 3)
# a = list(a)
# print(a, type(a))  # [1, 2, 3] <class 'list'>
# a.append(100)
# a.reverse()
# print(a, type(a))  # [100, 3, 2, 1] <class 'list'>
# a = tuple(a)
# print(a, type(a))  # (100, 3, 2, 1) <class 'tuple'>

# Так как кортеж это последовательность, мы можем обходить ее с помощью цикла For
# a = (1, 2, 3, 100, 32)
# for i in a:
#     print(i)  # в данном случае мы проходимся по значениям

# a = (1, 2, 3, 100, 32, 'hello')
# for i in range(len(a)):  # можно пройтись и по индексу [i] и по значению a[i]
#     print(a[i])


# ------------------------------------------------------------------
# УРОК № 5
# НОВАЯ ТЕМА
# МНОЖЕСТВА - SET

