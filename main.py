from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
screen.colormode(255)
screen.screensize(700, 700)
ypos = 240
tim.hideturtle()

def rand_color():
    for rando in range(0,3):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        rgb = (r, g, b)
    return rgb


def row_dots():
    for a in range(10):
        tim.speed("fastest")
        tim.dot(90, rand_color())
        tim.forward(50)

    
def next_row(y):
    tim.penup()
    tim.setpos(-240, y)


for dots in range(10):
    next_row(ypos)
    row_dots()
    ypos -= 50
        

screen.exitonclick()