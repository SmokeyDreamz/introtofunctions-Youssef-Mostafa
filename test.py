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

#rectangle code for challenge

""" t.forward(100)
t.left(90)
t.forward(125)
t.left(90)
t.forward(100)
t.left(90)
t.forward(125)
t.left(90) """

# triangle code for challenge

""" def equal(x):
    t.forward(x)
    t.left(120)
    t.forward(x)
    t.left(120)
    t.forward(x)
equal(90)  """




""" def equal(x):
    t.forward(x)
    t.left(120)
    t.forward(x)
    t.left(120)
    t.forward(x)
equal(90)  """



#star code for challenge

def star(x, y):
    for i in range(5):
        t.forward(x)
        t.left(y) 


def addStars(iRange):
    length = 5
    for i in range(iRange):
        star(length, 144)
        length += 5
        t.right(5)
addStars(60)


#Square spiral loop assesment


""" def square(x, y):
    for i in range(5):
        t.forward(x)
        t.left(y)

sidelength = 100
rotate = 90
def square(x,y):
    for i in range(4):
        t.forward(x)
        t.left(y)


def addSquares(iRange):
    length = 5
    for i in range(iRange):
        square(length, 90)
        length += 5
        t.right(5)
addSquares(60) """












turtle.done()
