import turtle
sc = turtle.Screen()
sc.bgcolor("orange")
sc.setup(400, 300)
sc.title("Welcome to the Turtle Window")
board = turtle.Turtle()
for i in range(4):
    board.forward(100)
    board.left(90)
    i = i + 1