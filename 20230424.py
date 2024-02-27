'''
#문제1
for i in range(20):
    if(i%2!=0 and i%5!=0):
        print(i, "段(단)")
        for n in range(10):
            if(n>0): print(n*i, end=" ")
        print("\033[31m"+"\n====================="+"\033[0m")
        
#문제2
num=0
n=int(input("n의 값을 입력하시오: "))

for i in range(n+1):
    num+=i**2
    print(i**2, "::", num)

print("계산값은 %d입니다." % num)


#문제3
print("사이다-700원 콜라-800원 물-1200원")
money=int(input("얼마를 입력하시겠습니까? : "))
c=int(input("선택) 1-사이다 2-콜라 3-물 : "))
if(c==1):
    print("사이다가 나왔습니다, 덜컹")
    money-=700
elif(c==2):
    print("콜라가 나왔습니다, 덜컹")
    money-=800
elif(c==3):
    print("물이 나왔습니다, 덜컹")
    money-=1200
print("잔돈 %d원 반환합니다." % (money))


#문제4
stu=[160, 600, 930, 599, 990]

print("""학생 토익점수은 아래와 같습니다.
최종선발(3차) 5명중 3명:""", stu)

print("""
+-------------------------------------+
2023년 3회(최종선발) 'TOEIC'시험 result
+-------------------------------------+
""")

for i in range(len(stu)):
    if(stu[i]>=850):
        print(i+1, "번 학생은 1급(최종합격) 입니다.")
    elif(stu[i]>=600):
        print(i+1, "번 학생은 2급(최종합격) 입니다.")
    else:
        print(i+1, "영어를 해야되 말아야 돼!!!")
print("-------------------------------------")

#문제5
import turtle as t
import math

t.shape("turtle")

#y축
t.lt(90)
t.fd(250)
t.write("Y 좌표")
t.fd(-500)
t.penup()
t.home()
t.pendown()
#x축
t.setheading(0)
t.fd(400)
t.write("X 좌표")
t.fd(-550)
t.penup()
t.home()
t.pendown()

t.color("blue")
t.pensize(4)
#파란거
for x in range(0, 360) :
    t.goto(x, 200*math.sin(x*3.14/180))

t.penup()
t.home()
t.pendown()
#빨간거
t.color("red")
for x in range(0, 360) :
    t.goto(x, 100*math.sin(x*3.14/180))

'''






