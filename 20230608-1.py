'''
score=[1,2,3,4,5]

sum=0
i=0
while i<5:
    sum+=score[i] #10번줄과 동일
    i+=1 #for문처럼 끝에 1더해주기
    #0,1,2,3,4
    
print(sum)

for i in range(0, 5, 1):
    sum+=score[i] 


xlist=list(range(0,10,1))

ylist=[ 5*x+10 for x in xlist ]
"""
print(xlist)
print(ylist)

for x in xlist:
    y=5*x+10
    ylist.append(y)
"""
print(xlist)
print(ylist)


import random as r
print("###############\n# 오늘의 속담 #\n###############")
속담=["사람은 사랑할 때 누구나 시인이 된다",
    "꿈을 지녀라. 그러면 어려운 현실을 이길 수 있다.",
    "고생없이 얻을 수 있는 진실로 귀중한 것은 하나도 없다.",
    "시작이 반이다."]
print(r.choice(속담))


import math as m
import turtle as t

xlist=list(range(0,721,10))
ylist=[m.sin(m.radians(x)) for x in xlist]
print(ylist)

for i in range(len(xlist)):
    x=xlist[i]
    y=ylist[i]
    t.goto(x, y*150)
    print("%3d도 --> %6.2f"%(x,y))

#--------------------------------
import sys
n=[]
while True:
    inp=input("친구 이름 입력: ")
    if inp=="0":
        print("등록완료")
        print("입력된 순서:", n)
        n.sort()
        print("정렬된 순서:", n)
        sys.exit()#종료
    else:
        n.append(inp)
        


import random as r
국=[r.randint(1,100) for x in range(10)]
수=[r.randint(1,100) for x in range(10)]
영=[r.randint(1,100) for x in range(10)]

국합=0
수합=0
영합=0

print("번호 국어 영어 수학\n----------------------")

for i in range(10):#번호별로 리스트 안 값 한줄씩 10번 출력
    국합+=국[i]
    영합+=영[i]
    수합+=수[i]
    
    print(" %2d  %3d  %3d  %3d" % (i+1, 국[i], 영[i], 수[i]))

#for x in 국:
#    국합+=x

print("----------------------")
print("평균 %3.1f %3.1f %3.1f" %(국합/10, 영합/10, 수합/10))

fp=open("D:\Rleadme\PythonStudy\\test.txt", "w")
fp.write("아\n아아\n아아아")
fp.close()
fp=open("D:\Rleadme\PythonStudy\\test.txt", "r")

print(fp.readline())
print(fp.readlines())


while 1:
    line=fp.readline()
    if len(line)==0:break
    print(line, end="")
fp.close()

#--------
import turtle as t

pos=[[0,0,"blue"],
     [-120,0,"purple"],
     [60,60,"red"],
     [-60,60,"yellow"],
     [-180,60,"green"]]

for i in range(len(pos)):
    t.color(pos[i][2])
    t.penup()
    t.goto(pos[i][0], pos[i][1])
    t.pendown()
    t.begin_fill()
    t.circle(30)
    t.end_fill()

import random as r
rlist=[0,0,0,0,0,0]

for i in range(1000):
    ran=r.randint(0,5)
    rlist[ran]+=1#리스트에 추가

for i in range(6):
    print("주사위가", i+1, "인 경우는", rlist[i], "번")

import turtle as t
clist=["yellow", "red", "purple", "blue"]

for i in range(len(clist)):
    t.fillcolor(clist[i])
    t.begin_fill()
    for n in range(4):
        t.fd(100)
        t.rt(90)
    t.end_fill()
    t.fd(100)

#실행결과 예측
a=10
def func(num = a): #num = 10
    print("num =", num)

func()
func(20)
a=30
func()
a=40
func(a)

'''
#실행결과 예측2
a=10
def func():
    global a
    a=5
    print(a)

print(a)
func()
print(a)


