import turtle  # turtle - название библиотеки

# В начале мы должны задать параметры как  shape (форма) color and speed
# turtle.shape ("turtle") # В скобках также писать arrow,circle,triangle


# turtle.forward(30)
# turtle.right(90)
# turtle.forward(30)
# turtle.right(90)
# turtle.forward(30)

# turtle.forward(size)
# turtle.right(angle)
# turtle.forward(size)
# turtle.right(angle)
# turtle.forward(size)

# angle = int(input("введите количество углов: "))
# size = int (input("введите длину стороны: "))
# color = input("напишите цвет,который вы хотите использовать: ")


turtle.shape("arrow")
turtle.color("red")
turtle.speed(3)
size = 200
angle = 5  # или 9 углов

if angle == 5:
    turtle.forward(size)
    turtle.left(143)
    turtle.forward(size)
    turtle.left(143)
    turtle.forward(size)
    turtle.left(143)
    turtle.forward(size)
    turtle.left(143)
    turtle.forward(size)
elif angle == 9:
    turtle.forward(size)
    turtle.left(160)
    turtle.forward(size)
    turtle.left(160)
    turtle.forward(size)
    turtle.left(160)
    turtle.forward(size)
    turtle.left(160)
    turtle.forward(size)
    turtle.left(160)
    turtle.forward(size)
    turtle.left(160)
    turtle.forward(size)
    turtle.left(160)
    turtle.forward(size)
    turtle.left(160)
    turtle.forward(size)
else:
    print("такой фигуры не существует")
