#1번 문제

a=3
b=2
c=4

a=b+c
print(a,b,c)

a=b//c
print(a,b,c)

#a+b=c #대입 연산자의 왼쪽에는 변수만 위치
print(a,b,c)

a=b+1
print(a,b,c)

b+=2
print(a,b,c)

#a=a%%c #나머지를 구할땐 % 하나만 사용 

#2번 문제

a=int(input("숫자1 : "))
b=int(input("숫자2 : "))
print(a, "/", b, "=", a/b)
print(a, "//", b, "=", a//b)
print(a, "%", b, "=", a%b)

#3번 문제

import math
radius=int(input("반지름 : "))
print("원의 넓이 : ", radius*radius*3.141592)
#print("원의 넓이 : ", radius*radius*math.pi)

#4번 문제
sec=int(input("초 : "))
minute=sec//60
second=sec%60
print(sec, "초 =", minute, "분", second, "초")

#5번 문제

a=int(input("정수 : "))
b=c=d=a #대입 순서 b=(c=(d=a)) 
print(a, b, c, d)

#6번 문제

#복합 대입 연산자를 사용한 수식
a+=b
a*=b
a*=(b+c)
a-=b*c

#결과 값
5
6
18
-5

#7번 문제

4-2/3
(1+2)/(2+4)
3*2/(4-2/3)
