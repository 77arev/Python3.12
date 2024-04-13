class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_perimetr(self):
        return 2 * (self.w + self.h)


if __name__ == '__main__':  # проверка
    r1 = Rectangle(1, 2)
    r2 = Rectangle(3, 4)
    print(f"Периметр прямоугольника: {r1.get_perimetr()}")
    print(f"Периметр прямоугольника: {r2.get_perimetr()}")


# print(__name__)  # __main__
# if __name__ == '__main__':
# Когда Python запускает скрипт, он устанавливает специальную переменную
# __name__ для этого скрипта в значение "__main__". Это означает, что скрипт
# запущен как основная программа.

# __author__ = "Admin"  # просто переменная
# if __name__ == '__main__':
#     print(f"Module {__name__} (author: {__author__})")
    # если делаем запуск с этого документа (rect.py), то все, что оказалось под (if),
    # оно отработает, а с дока (main) не отработает
