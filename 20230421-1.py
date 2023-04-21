import turtle as t
'''
t.color("blue")
t.pensize(5)
t.shape("turtle")
t.fd(100)
t.rt(180-45)
t.fd(100)
t.lt(180-45)
t.fd(100)


t.color("black")
t.begin_fill()
for i in range(4):
    t.forward(150)
    t.right(90)

t.end_fill()


width=int(t.textinput("직사각형", "가로 길이를 입력하세요."))
height=int(t.textinput("직사각형", "세로 길이를 입력하세요."))

t.shape("turtle")
t.fillcolor("orange")
t.begin_fill()
t.fd(width)
t.rt(90)
t.fd(height)
t.rt(90)
t.fd(width)
t.rt(90)
t.fd(height)
t.rt(90)
t.end_fill()
t.write("직사각형의 넓이는 %d입니다." %(width*height))


r=int(t.textinput("원넓이", "반지름을 입력하세요."))
t.fillcolor("skyblue")
t.begin_fill()
t.circle(200)
t.end_fill()
t.fd(100)
t.write("반지름이 %d인 원의 넓이는 %d입니다." % (r, r**2*3.14))
'''


for i in range(3):
    t.circle(100)
    t.penup()
    t.fd(150)
    t.pendown()
t.penup()
t.rt(90)
t.lt(90)
t.fd(-150)

t.pendown()
for i in range(2):
    t.circle(100)
    t.penup()
    t.fd(150)
    t.pendown()



