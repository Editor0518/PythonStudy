'''
text="Hello Python"
new=""
for i in text:
    new+= chr(ord(i)+10)

print(new)

import turtle as t
def draw_hexa():
    for i in range(6):
        t.fd(100)
        t.lt(60)


for i in range(6):
    draw_hexa()
    t.fd(100)
    t.rt(60)
'''

text= input("문자열 --> ")

x=text.split(" ")

for i in x:
    for a in range(10):
        if(x.find):




