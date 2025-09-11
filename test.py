import turtle
from turtle import *
t = Turtle()

t.shape('turtle')
t.speed(100)
""" def square(x):
    for i in range(60):
        t.forward(x)
        t.left(90)
        t.forward(x)
        t.left(90)
        t.forward(x)
        t.left(90)
        t.forward(x)
        t.left(90)
        t.right(5)
square(200) """



""" t.forward(100)
t.left(90)
t.forward(125)
t.left(90)
t.forward(100)
t.left(90)
t.forward(125)
t.left(90) """

""" def equal(x):
    t.forward(x)
    t.left(120)
    t.forward(x)
    t.left(120)
    t.forward(x)
equal(90)  """





def star(x, y):
    for i in range(5):
        t.forward(x)
        t.left(y)

""" def doubleSquares(iRange):
    sidelength = 25
    for i in range(iRange):
        square(sidelength)
        sidelength = sidelength * 2
doubleSquares(5) """


def addStars(iRange):
    length = 5
    for i in range(iRange):
        star(length, 144)
        length += 5
        t.right(5)
addStars(60)


""" def message(input):
    print(input)
message("Hello Class") """


""" def square(x, y):
    def addSquares(iRange):
        length = 25
    for i in range(iRange):
        square(length, 90)
        length += 25
        square(50)
    addSquares(5) """

""" def square(x):
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
square(200)

print(i) """

turtle.done()
