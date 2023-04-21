import turtle as t
s=0.4
t.speed(100000)

#창문 그리는 함수
def drawWindow(w, h):
    pos=t.pos()
    t.setheading(0)
    #바깥창문
    t.color("#DF727C")
    drawSquare(w, h)
    #안쪽창문
    t.color("#FDF2B4")
    moveX(10)
    drawSquare(w-20, h-30)
    #밑쪽네모
    moveY(8)
    moveX(-11-8)
    t.color("#F2B5C0")
    drawSquare(w+16, -10)
    moveX(8)
    moveY(-8)
    #창문 밑 눈 사다리꼴
    t.color("#E2DAE8")
    drawTrapzoid(w, w+16, 8)
    t.goto(pos)
    moveX(10)
    #안쪽 창문 커튼
    t.color("#A85B8B")
    for i in range(2):
        drawSquare((w-20)/4, h-30)
        moveX(w-20-((w-20)/4))
    t.color("#C6747D") #창
    t.penup()
    t.goto(pos)
    t.pendown()
    moveX(10)
    moveY(-(h-30-42))
    #창틀 가로프레임
    for i in range(2):
        drawSquare(w-20, 5)
        moveY(42)
    #이동
    t.penup()
    t.goto(pos)
    t.pendown()
    moveY(-(h-30))
    moveX(10+((w-20)/3))
    #창틀 세로프레임
    for i in range(2):
        drawSquare(5, -(42*2))
        moveX((w-20)/3)
    t.penup()
    t.goto(pos)
    t.pendown()


#위쪽 긴 창문 그리는 함수
def drawTopWindow(w, h):
    pos=t.pos()
    t.setheading(0)
    #바깥창문
    t.color("#DF727C")
    drawSquare(w, h)
    #안쪽창문
    t.color("#FDF2B4")
    moveX(10)
    drawSquare(w-20, h-15)
    #밑쪽네모
    moveY(8)
    moveX(-11-8)
    t.color("#F2B5C0")
    drawSquare(w+16, -10)
    moveX(8)
    moveY(-8)
    #창문 밑 눈 사다리꼴
    t.color("#E2DAE8")
    drawTrapzoid(w, w+16, 8)
    t.goto(pos)
    moveX(10)
    #안쪽 창문 커튼
    t.color("#A85B8B")
    for i in range(2):
        drawSquare((w-20)/6, h-15)
        moveX(w-20-((w-20)/6))
    t.color("#C6747D") #창
    t.penup()
    t.goto(pos)
    t.pendown()
    moveX(10)
    moveY(-(h-15-21))
    #창틀 가로프레임
    drawSquare(w-20, 5)
    
    #이동
    t.penup()
    t.goto(pos)
    t.pendown()
    moveY(-(h-15))
    moveX(10+((w-20)/3))
    #창틀 세로프레임
    for i in range(2):
        drawSquare(5, -(42*2))
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
    t.color("#D47A71")
    drawSquare(36, 120)
    moveX(5)
    moveY(-10)
    t.color("#F4F9B4")
    winX=t.pos()[0]
    winY=t.pos()[1]
    drawSquare(26, 100)
    t.color("#CC5865")
    for i in range(2):
        moveY(-(100/3))
        drawSquare(26, 3)
    movePos(winX+(13/2-1.5), winY)
    drawSquare(3, 100)

#문짝 그리기
def door():
    t.color("#643D35")
    drawSquare(78, 143)
    moveX(10)
    t.color("#000000")
    drawSquare(58, 134)
    moveX(6)
    t.color("#3C3023")
    drawSquare(46, 129)
    t.color("#311E13", "#492D20")
    moveX(2+2)
    moveY(-10)
    drawSquare(41-4, 42)
    moveY(-43)
    moveX(41)
    t.color("#D3C5AC", "#D3C5AC")
    drawSquare(1, 7)
    moveX(-41)
    moveY(-5)
    t.color("#311E13", "#3C3023")
    drawSquare(41-4, 42)
    moveY(-48)
    drawSquare(42-4, 18)

#바닥 눈 그리기
def drawBackFloor():
    t.setheading(90)
    movePos(x+3000+400, y-3000+50)
    t.color("gray")
    t.begin_fill()
    t.circle(3000, 180)
    t.end_fill()
    movePos(x,y)
    t.setheading(0)



# 지붕 만드는 함수 
def rooftopL():
    t.color("#87B4DD")
    t.begin_fill()
    t.goto(x1+330*s, y1+411*s)
    t.goto(x1+330*s, y1+(411+48)*s)
    t.goto(x1+(330-573)*s, y1+(411+48-25)*s)
    t.goto(x1+(330-573-157)*s, y1+(411+48-25-162)*s)
    t.goto(x1+(330-573-157)*s, y1+(0)*s)
    t.end_fill()

    t.color("gray")
    movePos(x1+330*s, y1+(411+48)*s)
    t.begin_fill()
    t.goto(x1+(330+300-20)*s, y1+(411+48-455)*s)
    t.goto(x1+(330+300-25-20)*s, y1+(411+48-455)*s)
    t.goto(x1+(330-20)*s, y1+(411)*s)
    t.end_fill() #오른쪽 지붕 선 그림자
    
    t.color("#D1D1DE")
    movePos(x1, y1)
    t.begin_fill()
    t.goto(x1, y1+44*s)
    t.goto(x1+330*s, y1+(411+48)*s)
    t.goto(x1+330*s, y1+(411)*s)
    t.goto(x1, y1)
    t.end_fill()#왼쪽 지붕 선 완료

    t.color("#D1D1DE")
    movePos(x1+330*s, y1+(411+48)*s)
    t.begin_fill()
    t.goto(x1+(330+300)*s, y1+(411+48-455)*s)
    t.goto(x1+(330+300-25)*s, y1+(411+48-455)*s)
    t.goto(x1+330*s, y1+(411)*s)
    t.end_fill() #오른쪽 지붕 선 완료
    movePos(x1, y1)
    
    t.color("#95BED7")
    t.begin_fill()
    t.goto(x1-50, y1)
    t.goto(x1-50, y1+44*s)
    t.goto(x1, y1+44*s)
    t.end_fill() #공백 채우기 
    
    t.color("#410D13")
    movePos(x1-107*s, y1+(471+13)*s)
    t.begin_fill()
    t.goto(x1-107*s, y1+(484+40)*s)
    t.goto(x1+(-107+10)*s, y1+(484+40)*s)
    t.goto(x1+(-107+10)*s, y1+(484)*s)
    t.end_fill()#막대 1 가운데 
    t.begin_fill()
    movePos(x1-(107+49)*s, y1+(273+198+10)*s)
    t.goto(x1-(107+49)*s, y1+(481+40)*s)
    t.goto(x1-(107+49)*s, y1+(481+40)*s)
    t.goto(x1-(107+49-10)*s, y1+(481+40)*s)
    t.goto(x1-(107+49-10)*s, y1+(273+198+10)*s)
    t.end_fill()#막대 2 왼쪽
    t.begin_fill()
    movePos(x1-(107-78)*s, y1+(273+198+10)*s)
    t.goto(x1-(107-78)*s, y1+(273+198+10+40)*s)
    t.goto(x1-(107-78)*s, y1+(273+198+10+40)*s)
    t.goto(x1-(107-78+10)*s, y1+(273+198+10+40)*s)
    t.goto(x1-(107-78+10)*s, y1+(273+198+10)*s)
    t.end_fill()#막대 3 오른쪽

    movePos(x1-107*s, y1+273*s)
    t.color("#533367")
    t.begin_fill()
    t.goto(x1-(107+49)*s, y1+(273)*s)
    t.goto(x1-(107+49)*s, y1+(273+198)*s)
    t.goto(x1-(107)*s, y1+(273+198)*s)
    t.end_fill() #굴뚝 옆면 완료 
    t.color("#AF301D")
    t.begin_fill()
    t.goto(x1-(107-78)*s, y1+(273+198)*s)
    t.goto(x1-(107-78)*s, y1+(273+198-95)*s)
    t.goto(x1-107*s, y1+273*s)
    t.end_fill()#굴뚝 아래 완성
    movePos(x1-(107+49)*s, y1+(273+198)*s)#=x1-(156), y1+(471)
    t.color("#4E5681")
    t.begin_fill()
    t.goto(x1-(156+10)*s, y1+(471)*s)
    t.goto(x1-(156+10)*s, y1+(471+13)*s)
    t.goto(x1-107*s, y1+(471+13)*s)
    t.goto(x1-107*s, y1+(471)*s)
    t.end_fill()#굴뚝 돌 벽면 완료 
    t.color("#6989C4")
    t.begin_fill()
    t.goto(x1-(29-10)*s, y1+(471)*s)
    t.goto(x1-(29-10)*s, y1+(471+13)*s)
    t.goto(x1-107*s, y1+(471+13)*s)
    t.goto(x1-107*s, y1+471*s)
    t.end_fill()#굴뚝 돌 앞면 완료
    
    movePos(x1-(156+10)*s, y1+(471+40)*s)
    t.color("#3F4A68")
    t.begin_fill()
    t.goto(x1-(156+10)*s, y1+(471+40)*s)
    t.goto(x1-(156+10)*s, y1+(471+13+40)*s)
    t.goto(x1-107*s, y1+(471+13+40)*s)
    t.goto(x1-107*s, y1+(471+40)*s)
    t.end_fill()#굴뚝 위 돌 벽면 완료 
    t.color("#72A2DD")
    t.begin_fill()
    t.goto(x1-(29-10)*s, y1+(471+40)*s)
    t.goto(x1-(29-10)*s, y1+(471+13+40)*s)
    t.goto(x1-107*s, y1+(471+13+40)*s)
    t.goto(x1-107*s, y1+(471+40)*s)
    t.end_fill()#굴뚝 위 돌 앞면 완료
    
    movePos(x1, y1)
    t.color("#A0CAF0")
    t.begin_fill()
    t.goto(x1-92*s, y1+273*s)
    t.goto(x-(60)*s, y1+(273)*s)
    t.goto(x+116*s, y1)
    t.goto(x1, y1)
    t.end_fill() #왼쪽 큰 지붕 베이스 완료 

## 함수 만드는 칸 종료 ##
 

#drawSquare(1356, 274)

t.bgcolor("#C8B2A6")
x=t.pos()[0]
y=t.pos()[1]

drawBackFloor()

#끝집
t.color("#533367")
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
t.color("#5E7AA9")
drawSquare(131, 23)#하얀 바닥베이스
moveY(-85)
drawWindow(72, 161)

#중간집
t.color("#AE3048")
movePos(newX,y)
newX=t.pos()[0]
drawSquare(620, 320)#빨간부분
t.color("#BBD2FB")
drawSquare(620, 23)#하얀 바닥베이스
newX=t.pos()[0]+620*s
moveX(107)
moveY(-85)
drawWindow(94, 189)
moveX(307)
drawWindow(94, 189)
movePos(newX,y)
t.color("#533367")
drawSquare(17, 320)#약간 짙은 빨간(깊이)
t.color("#6182B4")
drawSquare(17, 23)#약간 짙은 하얀 바닥베이스
moveX(17)
newX=t.pos()[0]

#빨간 오각형
t.begin_fill()
t.color("#AE3048")
t.fd(601*s)
newXend=t.pos()[0]
t.lt(90)
t.fd(320*s)
t.goto(newXend-277*s, t.pos()[1]+400*s)
t.goto(newX, t.pos()[1]-400*s)
t.goto(newX, y)
t.end_fill()
t.color("yellow")#BBD2FB
drawSquare(23, -601)#하얀 바닥베이스

#창문들
movePos(newX+74*s, y+85*s)
drawWindow(94, 189)
t.setheading(0)
moveX(94+86)
drawWindow(94, 189)
movePos(newX+239*s, y+406*s)
drawTopWindow(150, 95)

movePos(newXend-200*s, y)

#작은 문 있는 공간
t.color("blue")##922832
drawSquare(104, 174)
newX=t.pos()[0]
moveX(104)
t.color("green")##AF2942
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
t.color("#603C4E")
drawSquare(104, 10)
moveX(104)
#가운데 줄 문쪽
t.color("#DBBCD4")
drawSquare(200, 10)
movePos(newXend, y)
#맨끝에 물 배수구
t.color("#FAFEF5")
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
#####

#####
"""
movePos(x, y+571*s)
y1=t.pos()[1]
"""
#지붕 첫 레이어 값 저장
movePos(x+776*s, y+293*s)
x1=t.pos()[0] #t.goto(x1, y1)
y1=t.pos()[1]


rooftopL()

movePos(x, y)
t.color("#C8B2A6")
t.begin_fill()
for i in range(2):
    t.lt(90)
    t.fd(800)
    t.lt(90)
    t.fd(100)
t.end_fill()

movePos(x, y)
t.color("black")

movePos(newX-20*s, 170*s)
#지붕1
t.color("yellow")
t.begin_fill()
t.goto(t.pos()[0]-10*s, t.pos()[1]+15*s)
t.goto(t.pos()[0]+110*s, t.pos()[1]+120*s)
moveX(125)
t.goto(t.pos()[0]+110*s, t.pos()[1]-110*s)
t.goto(t.pos()[0]-16*s, t.pos()[1]-13*s)
t.goto(t.pos()[0]-93*s, t.pos()[1]+87*s)
movePos(newX+110*s, 170*s)
t.end_fill()
#지붕2
t.color("purple")
t.begin_fill()
movePos(newX+95*s, 170*s)
t.goto(t.pos()[0]-10*s, t.pos()[1]+13*s)
t.goto(t.pos()[0]+120*s, t.pos()[1]+117*s)
t.goto(t.pos()[0]+110*s, t.pos()[1]-110*s)
t.goto(t.pos()[0]-15*s, t.pos()[1]-13*s)
t.goto(t.pos()[0]-93*s, t.pos()[1]+87*s)
t.end_fill()







"""
안쓰는거 추천
movePos(x+1250*s, y+273*s)
x3=t.pos()[0] #t.goto(x3, y3)
y3=t.pos()[1]
movePos(x3+107*s, y3+273*s)
t.goto(x3+(107+123)*s, y3+(273-108)*s)
"""


"""
t.goto(x1*s, y1*s)
movePos(x+330*s, y+466*s)
t.pos()[0]
"""

