#1번 문제

abc=14
#3ab=14 변수명 숫자로 시작
#a b=14 변수명 내부 띄어쓰기
#import=14 변수명 예약어 사용
import_var=14
test=14
#temp#=14 변수명에 특수문자
k31=14

#2번 문제

a=3
c=a+b+1 #오류 : b를 초기화하지않음

#3번 문제

a=3
b=2
c=1
a=a+1
b=b
c=a+b
c=c+1

print(a,b,c)
#4 2 7

#4번 문제

subject=input("과목 : ")
score=int(input("점수 : "))
print("선호 과목 : ", subject,", 희망 점수 : ", score)

#5번 문제

a=int(input("정수1:"))
b=int(input("정수2:"))
c=int(input("정수3:"))
print("정수1: ", a,"정수2:", b, "정수3:", c)
sum=a+b+c
avg=sum/3
print("합: ", sum, "평균: ", avg)

#6번 문제

a=int(input("정수:"))
b=str(a) #문자열로 변환
print (a, type(a), b, type(b))

#7번 문제

import turtle as t
t.shape("turtle")
radius=int(input("반지름: "))
t.circle(radius)
t.circle(radius,steps=4)

#8번 문제

import turtle as t
t.shape("turtle")
radius=int(input("반지름: "))
length=int(input("진행: "))
for i in range(3):
    t.circle(radius)
    t.forward(length)


