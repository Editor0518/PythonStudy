num=int(input())
'''
for i in range(num-1):
    for n in range(num-(i+1)):
        print(" ", end="")
    print("*", end="")
    for n in range(i):
        print(" ", end="")
    for n in range(i-1):
        print(" ", end="")
    if i>0: print("*", end="")
    print()
for n in range(num*2-1):
    print("*", end="")
'''



for i in range(num*2+1):
    for n in range(num*2+1):
        print("*", end="")
