import turtle as t
s=0.4
t.speed(1000)

#창문 그리는 함수
def drawWindow(w, h):
    pos=t.pos()
    t.setheading(0)
    #바깥창문
    t.color("orange")
    drawSquare(w, h)
    #안쪽창문
    t.color("yellow")
    moveX(10)
    drawSquare(w-20, h-30)
    #밑쪽네모
    moveY(8)
    moveX(-11-8)
    t.color("orange")
    drawSquare(w+16, -10)
    moveX(8)
    moveY(-8)
    #창문 밑 눈 사다리꼴
    t.color("grey")
    drawTrapzoid(w, w+16, 8)
    t.goto(pos)
    moveX(10)
    #안쪽 창문 커튼
    t.color("red")
    for i in range(2):
        drawSquare((w-20)/4, h-30)
        moveX(w-20-((w-20)/4))
    t.color("orange")
    t.penup()
    t.goto(pos)
    t.pendown()
    moveX(10)
    moveY(-(h-30-42))
    #창틀 가로프레임
    for i in range(2):
        drawSquare(w-20, 3)
        moveY(42)
    #이동
    t.penup()
    t.goto(pos)
    t.pendown()
    moveY(-(h-30))
    moveX(10+((w-20)/3))
    #창틀 세로프레임
    for i in range(2):
        drawSquare(3, -(42*2))
        moveX((w-20)/3)
    t.penup()
    t.goto(pos)
    t.pendown()
    
#이동함수
def moveX(distance):
    t.penup()
    t.fd(distance*s)
    t.pendown()

def moveY(distance):
    t.rt(90)
    t.penup()
    t.fd(distance*s)
    t.pendown()
    t.rt(-90)

#사다리꼴 그리는 함수
def drawTrapzoid(w1, w2, h):
    w1*=s
    w2*=s
    h*=s
    t.begin_fill()
    start=t.pos()
    t.fd(w1)
    triangle=((w1-w2)/2)
    posX=t.pos()[0]-triangle
    posY=t.pos()[1]-h
    t.goto(posX, posY)
    t.bk(w2)
    t.goto(start)
    t.end_fill()

#사각형 그리기
def drawSquare(w, h):
    t.begin_fill()
    for i in range(2):
        t.fd(w*s)
        t.lt(90)
        t.fd(h*s)
        t.lt(90)
    t.end_fill()

def movePos(posXn, posYn):
    t.penup()
    t.goto(posXn, posYn)
    t.pendown()


#문쪽 작은 창문 그리는 함수
def drawSmallWindow():
    t.color("orange")
    drawSquare(36, 120)
    moveX(5)
    moveY(-10)
    t.color("yellow")
    winX=t.pos()[0]
    winY=t.pos()[1]
    drawSquare(26, 100)
    t.color("orange")
    for i in range(2):
        moveY(-(100/3))
        drawSquare(26, 3)
    movePos(winX+(13/2-1.5), winY)
    drawSquare(3, 100)

#문짝 그리기
def door():
    t.color("#A9A9A9")
    drawSquare(78, 143)
    moveX(10)
    t.color("#000000")
    drawSquare(58, 134)
    moveX(6)
    t.color("#A9A9A9")
    drawSquare(46, 129)
    t.color("#000000", "#A9A9A9")
    moveX(2+2)
    moveY(-10)
    drawSquare(41-4, 42)
    moveY(-43)
    moveX(41)
    t.color("yellow", "yellow")
    drawSquare(1, 7)
    moveX(-41)
    moveY(-5)
    t.color("#000000", "#A9A9A9")
    drawSquare(41-4, 42)
    moveY(-48)
    drawSquare(42-4, 18)

##함수 만드는 칸 종료##
 

#drawSquare(1356, 274)

x=t.pos()[0]
y=t.pos()[1]

#끝집
t.color("black")
t.begin_fill()
#사다리꼴 부분
t.fd(131*s)
newX=t.pos()[0]
t.lt(90)
t.fd(296*s)
t.goto(x, y+476*s)
t.goto(x,y)
#사다리꼴 부분끝
t.setheading(0)
t.end_fill()
movePos(x,y)
t.color("grey")
drawSquare(131, 23)#하얀 바닥베이스
moveY(-85)
drawWindow(72, 161)

#중간집
t.color("red")
movePos(newX,y)
newX=t.pos()[0]
drawSquare(620, 320)#빨간부분
t.color("grey")
drawSquare(620, 23)#하얀 바닥베이스
newX=t.pos()[0]+620*s
moveX(107)
moveY(-85)
drawWindow(94, 189)
moveX(307)
drawWindow(94, 189)
movePos(newX,y)
t.color("black")
drawSquare(17, 320)#약간 짙은 빨간(깊이)
t.color("lime")
drawSquare(17, 23)#약간 짙은 하얀 바닥베이스
moveX(17)
newX=t.pos()[0]

#빨간 오각형
t.begin_fill()
t.color("red")
t.fd(601*s)
newXend=t.pos()[0]
t.lt(90)
t.fd(320*s)
t.goto(newXend-277*s, t.pos()[1]+400*s)
t.goto(newX, t.pos()[1]-400*s)
t.goto(newX, y)
t.end_fill()
#창문들
movePos(newX+74*s, y+85*s)
drawWindow(94, 189)
t.setheading(0)
moveX(94+86)
drawWindow(94, 189)
movePos(newX+239*s, y+406*s)
drawWindow(150, 95)

movePos(newXend-200*s, y)

#작은 문 있는 공간
t.color("black")
drawSquare(104, 174)
newX=t.pos()[0]
moveX(104)
t.color("green")
t.begin_fill()
t.setheading(0)
t.fd(200*s)
newXend=t.pos()[0]
t.lt(90)
t.fd(174*s)
t.goto(t.pos()[0]-(104*s), t.pos()[1]+100*s)
t.goto(newX+(104*s), t.pos()[1]-(100*s))
t.end_fill()
movePos(newX, y+42*s)
t.setheading(0)
#가운데 줄
t.color("gray")
drawSquare(104, 10)
moveX(104)
#가운데 줄 문쪽
t.color("white")
drawSquare(200, 10)
movePos(newXend, y)
#맨끝에 물 배수구
t.color("gray")
drawSquare(13, 200)
drawSquare(25, 20)
movePos(newX+114*s, y+50*s)
#창문들
moveX(10)
winPos=t.pos()
drawSmallWindow()
t.penup()
t.goto(winPos[0], y)
t.pendown()
#문
moveX(46)
door()
t.penup()
t.goto(winPos)
t.pendown()
moveX(126+5)
drawSmallWindow()



""""""

