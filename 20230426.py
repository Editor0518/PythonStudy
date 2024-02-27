'''name=input("이름이 뭐예요? ")
year=int(input("몇 년도에 태어났어요? "))

print("""안녕하세요 %s씨 반가워요.\n당신은 %d년에 태어났군요.
당신은 올해 %d살이 되었습니다.""" % (name, year, 2023-year+1))

print("=== 몸무게 제안 프로그램 ===")
h=float(input("키 입력 -> "))
print("키 %.1f cm에 대한 적정 몸무게는 %.1f kg입니다." % (h, (h-100)*0.9))

x=2019
y=153
print("%5d + %5d = %5d" % (x, y, x+y))
print("%5o + %5o = %5o" % (x, y, x+y))
print("%5x + %5x = %5x" % (x, y, x+y))
'''

'''
<포맷함수 사용>
"{}".format(값)
"{0} {1}".format(0번값, 1번값)
"{0:10,d}".format(정수값) <<< 쉼표 표기하는 정수, 10칸 공백
"{0:5,.2f}".format(정수값) <<< 쉼표 표기하는 실수, 5칸 공백, 소숫점2자리

{0:e} = 0번째값(지수1.000e+01)
{0:b} = 2진수
{0:o} = 8진수

for i in range(65, 91, 1):
    print("%c --- %d --- %s" % (chr(i), i, bin(i)))
for i in range(65, 91, 1):
    print("{0:d} --- {0:c} --- {0:08b}".format(i))


won=int(input("한화 금액 입력 --> "))
print("""입금액: {0:,d}원
환전액: {1:,d}달러""".format(won, int(won/1135)))

mon=int(input("저축액 입력 : "))
iza=mon*0.0375*0.15
wonri=mon+iza
print("""저축액: {0:,d}원
이자: {1:,.0f}원
원리금: {2:,.0f}원""".format(mon, iza, wonri))

num=int(input("정수 입력: "))
print("""십진수: {0:15d}
 2진수: {0:15b}
 8진수: {0:15o}
16진수: {0:15x}""".format(num))

x=int(input("정수1 입력: "))
y=int(input("정수2 입력: "))

print("""
{0:d}     + {1:4d} = {2:5d}
{0:d}     - {1:4d} = {3:5d}
{0:d}     * {1:4d} = {4:5d}
{0:d}     / {1:4d} = {5:5.2f}""".format(x, y, x+y, x-y, x*y, x/y))


x=float(input("실수1 입력: "))
y=float(input("실수2 입력: "))

print("""
{0:.2f}     + {1:6.2f} = {2:8.2f}
{0:.2f}     - {1:6.2f} = {3:8.2f}
{0:.2f}     * {1:6.2f} = {4:8.2f}
{0:.2f}     / {1:6.2f} = {5:8.2f}""".format(x, y, x+y, x-y, x*y, x/y))
'''

year=int(input("년도 입력: "))
if(year%4==0 and (year%100!=0 or year%400==0)):
    print("윤년입니다")
else:
    print("윤년아닙니다")


