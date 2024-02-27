'''
import sys

n=int(input("n: "))
m=int(input("m: "))
total=0

if n>m:
    print("시작수가 끝나는수보다 크면안돼요")
    sys.exit()

for i in range(n, m+1, 1):
    total+=i
print(total)

n=30
total=0

while n<=70:
    print(n)
    total+=n
    n+=3
    

print("결과", total)



total=0

for n in range(50, 101, 1):
    if n%5==0 or n%3==0:
        print(n)
        total+=n

print("결과", total)
'''




#실행결과 예측
a=10
def func(num = a):
    print("num =", num)

func()
func(20)
a=30
func()
a=40
func(a)

밝기21 백라이트10








