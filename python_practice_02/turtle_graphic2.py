import turtle
import random

#함수선언
def screenLeftClick(x,y):
    tSize = random.randrange(1,10)
    turtle.shapesize(tSize)
    
    r=random.random()
    g=random.random()
    b=random.random()
    
    turtle.color(r,g,b)

    tAngle = random.randrange(0,360)

    turtle.penup()
    turtle.goto(x,y)
    turtle.left(tAngle)
    turtle.stamp()


#변수선언
r,g,b = 0.0,0.0,0.0
tSize = 0
tAngle = 0

#main

turtle.title('거북이로 도장찍기')
turtle.shape('triangle')
turtle.onscreenclick(screenLeftClick, 1)

turtle.done()
