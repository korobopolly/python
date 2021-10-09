'''
#복합 대입 연산자
x=int(input("정수: "))
x+=2
print("x+=2")
print(x)

x-=2
print("x-=2")
print(x)

x*=2
print("x*=2")
print(x)

x/=2
print("x/=2")
print(x)

x//=2
print("x//=2")
print(x)

x%=2
print("x%=2")
print(x)


#1~10까지 자연수 합계 구하기
x=int(input("정수1: "))
y=int(input("정수2: "))
for i in range(10):
    x+=1
    y+=x
print (x,y)

a=1
b=2
c=3
c*=a-b #복합 연산자 < 일반 연산자 (우선순위)
print(c)


x=int(input("정수1: "))
y=int(input("정수2: "))
z=(x+y)/2
print("평균: ",z)
'''
a=(10+20+30+40+50)/5
print(a)

b=3+2*4/2
c=3+((2*4)/2)
print(b,c)
d=((3+2)*4)/2
print(d)
