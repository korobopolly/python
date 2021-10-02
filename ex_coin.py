'''
#필요 동전 계산기
x=int(input("금액 : "))
x500=x // 500
t=x % 500
x100=t // 100
t=t % 100
x50=t // 50
t=t % 50
x10=t //10

print("500원 : ", x500,"/","100원 : ", x100,"/","50원 : ", x50,"/","10원 : ", x10)

x=int(input("정수1: "))
y=int(input("정수2: "))
print(x/y)
print(x//y)
print(x%y)
'''
#다중 대입문
a=b=c=1
print(a)

x,y=3,4
x,y=y,x
print(x,y)
