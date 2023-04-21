'''
#연습4
너비=25
높이=15
넓이=너비*높이*0.5
print("== 삼각형 넓이 계산 ==")
print("너비:", 너비, "미터")
print("높이:", 높이, "미터")
print("삼각형 넓이:", 넓이, "제곱미터")

#연습9
print("파이썬은 쉽지만")

#파이썬은 쉽지만 매우 유용한, 프로그래밍 언어입니다.
#파이썬은 쉽지만
#매우 유용한,
#프로그래밍 언어입니다.
print('파이썬은 쉽지만', end="")
print('매우 유용한')
print('프로그래밍 언어입니다.')
'''
'''
x=2019
y="2000"
print(x, end="")
print(y)
print(x, y, sep="")

print(bin(1000))
print("{0:b}".format(-10))


letter="HELLO Python"
encodeLetter =""

for ch in letter:
    num=ord(ch)
    encodeLetter+=chr(num+3)

print(letter, "-->", encodeLetter)

#________________________________

decodeLetter=""

for ch in encodeLetter:
    num=ord(ch)
    decodeLetter+=chr(num-3)

print(encodeLetter, "-->", decodeLetter)


n=input("숫자를 입력하세요: ")

if n==1:
    print("n is 1")
else:
    print("n is not 1")

#input 값으로 1을 입력하면 무엇이 출력될까?
'''

num=0

for i in range(4):
    num+=1
print(num)
