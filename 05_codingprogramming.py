#1번 문제

a<3
#a=<b #a<=b 가 맞다
a>b
a<=3
a=b
#a<>b #a!=b 가 맞다

#2번 문제

print(3>2 or 2<-1) #True
print(2<-1 and 3>2) #False
print(2<-1 or 3>2) #True
print(3>2 and 2>-1) #True
print(2<-1 or 3<2) #False
print(not(3>2 and 2<-1)) #True
print(3>2 and 2<-1) #False
print(not(3>2 and 2>-1)) #False

#3번 문제

num=int(input("정수 : "))
if num<100:
    print(num)

#4번 문제

num=int(input("정수 : "))
if num%2==0:
    print("짝수")

#5번 문제

num=int(input("정수 : "))
if num%2==0:
    print("짝수")
elif num%2!=0:
    print("홀수")

#6번 문제

num=int(input("정수 : "))
if num<100:
    print(num*0.9)
else:
    print(num*1.1)

#7번 문제

a=int(input("a : "))
b=int(input("b : "))
tmp=a+b-b*b
if tmp==0 or tmp>=0:
    print(tmp)
else:
    print("음수")

#8번 문제

num=int(input("정수 : "))
if num%2==0 and num%3==0:
    print("나누어짐")
else:
    print("나누어지지 않음")

#9번 문제

a=5
b=3
operator=input("연산자 : ")
if operator=="+":
    print(a, "+", b, "=", a+b)
elif operator=="-":
    print(a, "-", b, "=", a-b)
elif operator=="*":
    print(a, "*", b, "=", a*b)
elif operator=="/":
    print(a, "/", b, "=", a/b)

#10번 문제

ph=int(input("ph : "))
if ph>=0 and ph<=4:
    print("강산성")
elif ph>=5 and ph<=6:
    print("약산성")
elif ph==7:
    print("중성")
elif ph>=8 and ph<=9:
    print("약염기성")
elif ph>=10 and ph<=14:
    print("강염기성")

#11번 문제

year=int(input("년도 : "))
if year%4==0 and year%100!=0:
    print("윤년")
elif year%4==0 and year%100==0 and year%400==0:
    print("윤년")
else:
    print("평년")

#12번 문제

height=int(input("키(cm) : "))
weight=int(input("몸무게(kg) : "))
height_m=height/100
bmi=weight/(height_m*height_m)
if bmi <18.5:
    print("저체중")
elif bmi >=18.5 and bmi<23:
    print("정상")
elif bmi >=23 and bmi<25:
    print("과체중")
elif bmi >=25 and bmi<30:
    print("경도비만")
elif bmi >=30 and bmi<35:
    print("중등도비만")
elif bmi >=35:
    print("고도비만")
