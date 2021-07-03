import turtle
turtle.shape("turtle")
turtle.shapesize(2)
turtle.color("green", "yellow")
turtle.width(3)
turtle.speed(100)
turtle.backward(300)
turtle.penup()

cell_size = 20
cells_in_row = 10
rows_number = 20  # обязательно чётное число!

for row in range(rows_number // 2):
    for step in range(2):
        for cell in range(cells_in_row):
            turtle.pendown()
            turtle.begin_fill()
            for edge in range(6):
                turtle.forward(cell_size)
                turtle.left(360 / 6)
            turtle.end_fill()
            turtle.penup()

            turtle.forward(cell_size * 3)
        turtle.backward(cell_size * 3 * cells_in_row - cell_size)
        turtle.right(60)
        turtle.forward(cell_size)
        turtle.left(60)
    turtle.backward(3 * cell_size)