#연습문제 11
cm=float(input("키를 입력하세요 : "))
kg=float(input("몸무게를 입력하세요 : "))
m=cm/100
bmi=kg/(m**2)

print("BMI : {0:.1f}".format(bmi))

if(bmi<20):#20미만 저체중
    print("저체중입니다.")
elif(bmi<25):#20~25미만 정상
    print("정상 BMI 수치입니다.")
elif(bmi<30):#25~30미만 과체중
    print("과체중(1도 비만)입니다.")
elif(bmi<=40):#30~40 비만
    print("비만(2도 비만)입니다.")
else:#40초과 고도비만
    print("고도비만(3도 비만)입니다.")
