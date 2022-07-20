# 터틀 모듈 import
import turtle

hexagonTurtle = turtle.Turtle()

hexagonTurtle.forward(150)
for i in range(5):
    hexagonTurtle.right(60)
    hexagonTurtle.forward(150)

turtle.done()