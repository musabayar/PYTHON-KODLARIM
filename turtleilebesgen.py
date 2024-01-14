import turtle
import random
import time
def polygon(sides,length,x,y,color):
    turtle.penup()
    turtle.setposition(x,y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for i in range(sides):
        turtle.forward(length)
        turtle.left(360//sides)
        turtle.end_fill()
    time.sleep(5)
polygon(5,100,50,50,"blue")


