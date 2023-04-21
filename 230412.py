"""
%d int
%f float
%g int of float (자동으로 표시)
%s str
%c char
%o 8진수 (0~7)
%x 16진수 (0~9, A,B,C,D,E,F)

양식문자 사용 이유
-소스코드 보기좋게
-실수는 소숫점 자릿수 지정 가능
-출력형태 깔끔
-8진수, 16진수로 표현 가능해서

.format함수

print("%d %d %05d" % (123, 123, 123))
print("{0:d} {1:5d} {2:05d}".format(123, 123, 123))

"""
"""
name="진소은"
age=19
weight=58.7
#원본
print("내 이름은", name, "입니다.")
print("나는", age, "살입니다.")
print("나의 몸무게는", weight, "kg입니다.")
#양식문자 쓰기
print("내 이름은 %s입니다." % name) #반점X
print("나는 %d살입니다." % age)
print("나의 몸무게는 %.2f kg입니다." %weight)

io=.000001
iooo=0
for i in range(1000000):
    iooo+=io
print(1.0==1)
print(int(iooo)==1)
print(iooo==1)
print("%.f을 몇번 더한 값은 %.20f 입니다." % (io, iooo))


print("%d" % 123)
print("%5d" % 1234567)
print("%5d" % 123)
print("%05d" % 123)
print("%05d" % 123)

print("%f" % 123.45)
print("%3f" % 123.45)
print("%7.1f" % 123.45)
print("%7.3f" % 123.45)


print("%s" % "Python")
#Python
print("%10s" % "Python")
#    Python
print("%  10s" % "Python")
#xxxxPython은 어떻게?


kor=90
eng="80점"
print("국어는 %d점이고 영어는 %s입니다" % (kor, eng))

x=7
y=8
print("%d와 %d를 곱한 값은 %d입니다." %(x, y, x*y))

x=10
y=3

print("%d와 %d를 나눈 값은 %.2f입니다. 몫이 %d이라는 소리죠." % (x, y, x/y, x/y))


print("%d,%5d,%05d" % (123, 456, 789))
print("{1:d},{0:5d},{2:05d}".format(123, 456, 789))
print("{1:d},{0:5d},{0:05d}".format(123, 456, 789))

print('''줄바꿈\n연습
\t탭키\t연습
글자가 \"강조\"되는 효과1
글자가 \'강조\'되는 효과2
\\\\\\ 역슬래시 세 개 출력
\\n \\t \\\" \\\\를 그대로 출력
''')

print("%d {1:d} {0:5d} %s {0:05d}".format(123, 456, 789) % (999, "Python"))



name=input("이름이 뭐예요? ")
year=int(input("몇 년도에 태어났어요? "))
print(
'''
안녕하세요. %s씨 반가워요.
당신은 %d년에 태어났군요.
당신은 올해 %d살이 되었습니다.
''' % (name, year, (2023-year+1)))

h=float(input("===몸무게 제안 프로그램===\n키입력 --> "))
print("%.1f cm에 대한 적정 몸무게는 %.1f kg 입니다."% (h, (h-100)*0.9))
print("{0:.1f} cm에 대한 적정 몸무게는 %.1f kg 입니다.".format(h) % ((h-100)*0.9))
#167.5 60.8


x=2019
y=153
print("%5d + %5d = %5d" % (x, y, x+y))
print("%5o + %5o = %5o" % (x, y, x+y))
print("%5x + %5x = %5x" % (x, y, x+y))

a=int(input("첫 번째 정수 입력: "))
b=int(input("두 번째 정수 입력: "))

print(a, " + ", b, " = ", (a+b))
print(a, " - ", b, " = ", (a-b))
print(a, " * ", b, " = ", (a*b))
print(a, " / ", b, " = ", (a/b))

print("%d + %d = %d" % (a, b, a+b))
print("%d - %d = %d" % (a, b, a-b))
print("%d * %d = %d" % (a, b, a*b))
print("%d / %d = %f" % (a, b, a/b))

print('''{0:d} + {1:d} = {2:d}
{0:d} - {1:d} = {3:d}
{0:d} * {1:d} = {4:d}
{0:d} / {1:d} = {5:f}
'''.format(a, b, a+b, a-b, a*b, a/b))

a=2019/13
b=10/3
print(a, " + ", b, " = ", (a+b))
print(a, " - ", b, " = ", (a-b))
print(a, " * ", b, " = ", (a*b))
print(a, " / ", b, " = ", (a/b))
print("using %______________")
print("%.2f + %.2f = %8.2f" % (a, b, a+b))
print("%.2f - %.2f = %8.2f" % (a, b, a-b))
print("%.2f * %.2f = %8.2f" % (a, b, a*b))
print("%.2f / %.2f = %8.2f" % (a, b, a/b))
print("using {  }______________")
print('''{0:.2f} + {1:.2f} = {2:8.2f}
{0:.2f} - {1:.2f} = {3:8.2f}
{0:.2f} * {1:.2f} = {4:8.2f}
{0:.2f} / {1:.2f} = {5:8.2f}
'''.format(a, b, a+b, a-b, a*b, a/b))
"""



print("=== 원리금 계산 프로그램 ===")
money=int(input("저축 금액 입력: "))
plus=money*.0375
tax=plus*.15
total=money+plus-tax
print('''원금: %10d원
이자: %10d원
세금: %10d원
최종: %10d원
''' % (money, plus , tax, total))

print("원금: %10d원"% money)
print("이자: %10d원"% plus)
print("세금: %10d원"% tax)
print("최종: %10d원"% total)


print('''원금: {0:10,.0f}원
이자: {1:10,.0f}원
세금: {2:10,.0f}원
최종: {3:10,.0f}원
'''.format(money, plus , tax, total))

"""
>>>x=10
>>>'x is {}'.format(20)
'x is 20'
>>>'x is {}'.format(x)
'x is 10'
'I am {} years old'.format(20)
'I am 20 years old'
'print {} and {}'.format(1, x)
'print 1 and 10'
#{}사이에 공백 들어가면 에러남
"""



