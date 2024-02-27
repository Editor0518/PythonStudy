'''

'''
import turtle

# 각종 설정
player = turtle.Turtle()
player.color("#FFBB00") #색깔 정하기 with RGB code
player.shape("turtle") #모양 정하기
player.speed(0) #속도는 숫자가 작을수록 빠름
screen = player.getscreen()
player.penup() # 펜 들기 == 그림 그리지 않는 상태

# left, right 는 각도 변경
def jump() :
    for i in range(25):
        player.goto(0, player.pos()[1]+2)
        
    for i in range(25):
        player.goto(0, player.pos()[1]-2)
    
def keepGo():
    print("아")
    player.goto((player.pos()[0]+2, player.pos()[1]))


# 최근동작 취소 (ctrl+z와 같은 동작)
def undo() :
    player.undo()

# 프로그램(창) 끈다
def endProgram() :
    screen.bye()

# onkeypress(함수명, 키보드버튼명) :
# 어떤 버튼을 눌렀을 때, 이 함수가 동작하도록 하겠다!
screen.onkeypress(jump, "space")
screen.onkeypress(jump, "Up")
screen.onkeypress(jump, "Down")
screen.onkeypress(endProgram, "q")
screen.listen() # 프로그램 활성화
screen.mainloop() # 프로그램이 계속 동작하는 상태를 유지하겠다!

while True:
    print("음")
    keepGo()
