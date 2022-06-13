import turtle
import random
from tkinter.simpledialog import *
import math

#전역변수
inStr =""
swidth,sheight=300,300
tX,tY,txtSize =[0]*3

#메인코드

turtle.title("거북이 글자 쓰기")
turtle.shape("circle")
turtle.setup(width = swidth + 50, height = sheight +50)
turtle.screensize(swidth,sheight)
turtle.penup()
inStr = askstring("문자열 입력","거북이 쓸 문자열을 입력")

#거리와 크기
dist =100
txtSize = 20
value = int(360/len(inStr))
angle=0

for ch in inStr:
    
    rad = 3.14 * angle/180
    tX= dist * math.cos(rad)
    tY= dist * math.sin(rad)
    angle = angle + value
    
    r=random.random(); g=random.random(); b=random.random();

    turtle.goto(tX,tY)
    turtle.pencolor(r,g,b)
    turtle.write(ch,font=("맑은 고딕",txtSize,'bold'))

turtle.done()
