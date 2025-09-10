import turtle
from turtle import *
t = Turtle()

t.shape('turtle')
t.speed(40)
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

def square(x):
    def addSquares(iRange):
        length = 25
    for i in range(iRange):
        square(length, 90)
        length += 25
addSquares(5)

square(50)

turtle.done()