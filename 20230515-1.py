'''
키보드 입력에 따라 거북이가 움직이며
그림도 그릴 수 있는 파이썬 프로그램입니다.
by 탐구소년
'''
from turtle import *

# 각종 설정
player = Turtle()
player.color("#FFBB00") #색깔 정하기 with RGB code
player.shape("turtle") #모양 정하기
player.speed(0) #속도는 숫자가 작을수록 빠름
screen = player.getscreen()
player.penup() # 펜 들기 == 그림 그리지 않는 상태

t1=Turtle()
t1.color("red")
t1.shape("turtle")
t1.speed(0) 
t1.pendown()


# left, right 는 각도 변경
def left() :
    player.left(10)
def right():
    player.right(10)

# forward, backward 는 거리 이동
def up() :
    player.forward(30)
def down() :
    player.backward(30)

def endProgram() :
    screen.bye()

# onkeypress(함수명, 키보드버튼명) :
# 어떤 버튼을 눌렀을 때, 이 함수가 동작하도록 하겠다!\

import time
t1.color("red")
t1.shape("square")
t1.speed(0) 
t1.pendown()
t2=Turtle()
t2.color("white")
t2.shape("square")
t2.speed(0) 
t2.pendown()

def square():
    t1.fd(1)
    t2.fd(1)

t1.setheading(-90)
t2.setheading(-90)
t2.goto(0, 20)
square()


#screen.onkeypress(up, "Left")
#screen.onkeypress(down, "Right")
#screen.onkeypress(endProgram, "q")
screen.listen() # 프로그램 활성화
#screen.mainloop() # 프로그램이 계속 동작하는 상태를 유지하겠다!

while True:
    square()
    screen.onkeypress(up, "Left")
    screen.onkeypress(down, "Right")





