# ДЗ №28 от 01.04.2024
# Задача:
# Создать класс Shape и три дочерних класса: Square, Rectangle, Triangle в Python. Родительский класс
# должен иметь абстрактные методы нахождения периметра, площади, рисования фигуры и вывода информации.
# С помощью полиморфизма реализуйте вывод информации о дочерних фигурах.

from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def info(self):
        pass


class Square(Shape):
    def __init__(self, side, color):
        super().__init__(color)
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return self.side * 4

    def draw(self):
        return ("*" * self.side + "\n") * self.side
        # return '\n'.join(['*' * self.side for _ in range(self.side)])

    def info(self):
        print("===Квадрат===")
        print("Сторона:", self.side)
        print("Цвет:", self.color)
        print("Площадь:", self.area())
        print("Периметр:", self.perimeter())
        # print(Square.draw(self))
        # print(self.draw())


class Rectangle(Shape):
    def __init__(self, length, width, color):
        super().__init__(color)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return (self.length + self.width) * 2

    def draw(self):
        return ("*" * self.width + "\n") * self.length

    def info(self):
        print("===Прямоугольник===")
        print("Длина:", self.length)
        print("Ширина:", self.width)
        print("Цвет:", self.color)
        print("Площадь:", self.area())
        print("Периметр:", self.perimeter())
        # print(Rectangle.draw(self))
        # print(self.draw())


class Triangle(Shape):
    def __init__(self, side1, side2, side3, color):
        super().__init__(color)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return round((s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5, 2)

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    def draw(self):
        return '\n'.join([' ' * (self.side2 - i) + '*' * (2 * i - 1) + ' ' * (self.side2 - i) for i in range(1, self.side2 + 1)])

    def info(self):
        print("===Треугольник===")
        print("Сторона 1:", self.side1)
        print("Сторона 2:", self.side2)
        print("Сторона 3:", self.side3)
        print("Цвет:", self.color)
        print("Площадь:", self.area())
        print("Периметр:", self.perimeter())


square = Square(3, "red")
print(square.info())
print(square.draw())

rectangle = Rectangle(3, 7, "green")
print(rectangle.info())
print(rectangle.draw())

triangle = Triangle(11, 6, 6, "yellow")
print(triangle.info())
print(triangle.draw())