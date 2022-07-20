import turtle   # turtle 모듈 import
# 별 만들기
# 터틀 객체 생성
starTurtle = turtle.Turtle()

starTurtle.right(72)
starTurtle.forward(200)
for i in range(4):
    starTurtle.right(144)
    starTurtle.forward(200)
turtle.done()
