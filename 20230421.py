print("== 적정 몸무게 안내 프로그램 ==")
키=int(input("키 입력: "))
print("당신의 키", 키, "cm에 대한 적정 몸무게: ", (키-100)*0.9, "kg")
print("---------")
print("== 원의 둘와 넓이 계산 ==")
반지름=float(input("원의 반지름 입력: "))
pi=3.141592
print("원의 넓이는", 반지름**2*pi, "입니다. \n원의 둘레는", 반지름*2*pi, "입니다.")
print("---------")
x=int(input("X를 입력하세요 > "))
y=int(input("Y를 입력하세요 > "))
print(x, "과", y, "를 곱한 값은", x*y, "입니다.")
print("---------")
print("== 인치 --> 센티미터 변환 프로그램 ==")
인치=int(input("인치 입력: "))
print(인치, "inch는", 인치*2.54, "cm 입니다.")
print("---------")
print("== 센티미터 --> 인치 변환 프로그램 ==")
센티=float(input("센티미터 입력: "))
print(센티, "cm는", 센티/2.54, "inch 입니다.")
print("---------")
import calendar
년도=int(input("출생년도 : "))
월=int(input("출생월 : "))
calendar.prmonth(년도, 월)
print("---------")
a=int(input("숫자1 입력: "))
b=int(input("숫자2 입력: "))
print(a, "+", b, "=", a+b)
print(a, "*", b, "=", a*b)
print(a, "^", b, "=", a**b)







