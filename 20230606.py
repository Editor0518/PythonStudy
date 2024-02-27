'''
#append
mark=[]
total=0

for i in range(10):
    score=int(input(str(i+1)+"번 학생의 성적을 입력하세요: "))
    mark.append(score)
    total+=score

print("성적의 합계:", total)
print("성적의 평균:", total/len(mark))

#not append
mark=[]
total=0

for i in range(10):
    score=int(input(str(i+1)+"번 학생의 성적을 입력하세요: "))
    mark[score]
    total+=(list(score))

print("성적의 합계:", total)
print("성적의 평균:", total/len(mark))




'''
'''
#프로그램 코드 완성
num = [100, 96, 209, 220, 300, 117]

for i in num:

    if i%2>0:
      print(i, end=", ")

#리스트로 입력받고 출력
      import sys
hero=[]
while True:
    name = input("영웅들의 이름을 입력하시오: ")
    if name=="":
        for x in hero:
            print(x, end=" ")
        sys.exit()
    else:
        hero.append(name)

score = int(input("성적을 입력하시오: "))

if score>=60:
    print("합격입니다.")
else:
    print("불합격입니다.")


#1. 실행 결과 예상
a=10
if a>0 and a<0:
    print(100)
else:
    print(200)

#2. 실행 결과 예상
a=10
if a>0 or a<0:
    print(100)
else:
    print(200)

#3. 실행 순서 예상
a=100

def PrintA():
    print(1)

print(2)
PrintA()

if a>10:
    print(3)

if a<0:
    print(4)
elif a==100:
    print(5)
else:
    print(6)

PrintA()
'''
'''
#4. 실행 결과 예상
def func(x):
    y=x+10
    return y

a=func(1)
print(a)

#5. 실행 결과 예상
def func(x):
    y=x+10
    return x

a=func(1)
print(a)

#6. 실행 결과 예상
def func(x=5):
    y=x+10
    return y

a=func(1)
print(a)

#7. 실행 결과 예상
def func(x=5):
    y=x+10
    return y

a=func()
print(a)

pi=3.14
def 둘레(r):
    c_len=2*r*pi
    print("반지름이 %3d인 원의 둘레는 %8.2f입니다." %(r, c_len))
def 넓이(r):
    c_area=r*r*pi
    print("반지름이 %3d인 원의 넓이는 %8.2f입니다." %(r, c_area))

둘레(10)
넓이(10)
둘레(15)
넓이(15)
둘레(20)
넓이(20)

#8. 실행결과 예상
def func(a):
    print(a)
    b=a+10
    return b
answer=func(100)
print(answer)
print("=============")

#9. 실행결과 예상
def func(a):
    b=a+10
    return b
print(func(func(func(100))))

def 학점(점수):
    if 점수>=90:
        return "A"
    elif 점수>=80:
        return "B"
    elif 점수>=70:
        return "C"
    elif 점수>=60:
        return "D"
    else:
        return "F"

while True:
    점수=int(input("점수 입력 : "))
    print("당신의 점수 :", 점수)
    print("당신의 학점 :", 학점(점수))
    print()

def func(x):
    y=x+10
#    return y
    #여기부터 다 실행 안함
    print("안녕하세요")
    #return x
print(type(func(1)))

#print(func(1))#None
#print(func(2))#12 2
#print(func(3))#13 3

def 짝홀(num):
    if num%2==0:
        return "짝수"
    else:
        return "홀수"

while True:
    n=int(input("양의 정수 입력: "))
    print(짝홀(n)+"입니다.")

a=list(range(10,101,10))
print(a)
print(type(a))

b=range(10,101,10)
print(b)
print(type(b))

#실행결과 예측
n=0
while n<10:
    print(n)
    n+=1 #n에 1을 더함
    for i in range(n): #0~(n-1)
        print(i, end=", ")
    if n>=5:
        n+=2
    print() #줄바꿈
'''


