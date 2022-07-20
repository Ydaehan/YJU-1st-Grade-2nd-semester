import turtle
# 눈꽃 만들기

snowTurtle = turtle.Turtle()
n = 120
turtle.bgcolor("BLACK")
snowTurtle.color("SKYBLUE")
snowTurtle.width(10)
snowTurtle.left(90)
for a in range(6):
    for i in range(3):
        snowTurtle.forward(n / 4)
        snowTurtle.left(60)
        snowTurtle.forward(60 - 10 * i)
        snowTurtle.backward(60 - 10 * i)
        snowTurtle.right(120)
        snowTurtle.forward(60 - 10 * i)
        snowTurtle.backward(60 - 10 * i)
        snowTurtle.left(60)
        if i >= 2 :
            snowTurtle.forward(n / 4)
            snowTurtle.backward(n)
    snowTurtle.right(120)
    snowTurtle.forward(60)
    snowTurtle.left(60)

turtle.done()