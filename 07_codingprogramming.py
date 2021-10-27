#1번 문제

def print_python():
    print("파이썬")
print_python()

#2번 문제

def welcome():
    for i in range(3):
        print("환영합니다.")
welcome()

#3번 문제

n=input("이름 : ")
def welcome(name):
    print("환영합니다.", name, "님")
welcome(n)

#4번 문제

s=input("문자열 :")
c=int(input("횟수 :"))
      
def print_str(st,cnt):
    for i in range(cnt):
        print(st)
print_str(s,c)

#5번 문제

n=input("이름 :")

def welcome(name, msg="환영합니다."):
    print(msg, name, "님")
welcome(n)
welcome(n,"반갑습니다.")

#6번 문제

n1=int(input("정수1 : "))
n2=int(input("정수2 : "))

def calc(num1,num2,act="+"):
        if act=="+":
           print(num1+num2)
        elif act=="-":
           print(num1-num2)
        elif act=="*":
           print(num1*num2)
        elif act=="/":
           print(num1/num2)
        else:
            print("잘못된 연산기호입니다.")
calc(n1,n2)
calc(n1,n2,"*")
calc(n1,n2,"^")

#7번 문제

n1=int(input("정수1 : "))
n2=int(input("정수2 : "))

def calc(num1,num2,act="+"):
        if act=="+":
           print(num1+num2)
        elif act=="-":
           print(num1-num2)
        elif act=="*":
           print(num1*num2)
        elif act=="/":
           print(num1/num2)
        else:
            print("잘못된 연산기호입니다.")
calc(n1,n2,"*")
calc(num1=n1,num2=n2,act="*") #키워드 인수 : 순서를 뒤바꾸어도 상관없음
calc(num2=n2,num1=n1,act="*")

#8번 문제

r=int(input("반지름 : "))
def circle_area(radius):
    res=radius*radius*3.141592
    print("반지름", radius, "의 넓이 : ", res)
circle_area(r)

#9번 문제

def pow_xy(x,y):
    res=x**y
    return res

print("3 * 2**4 + 5 = ",3*pow_xy(2,4)+5)

#10번 문제
t=int(input("온도 : "))
a=int(input("변환(0:C2F, 1:F2C) :"))
def fc(temper, action):
    if action==0:
        rt=temper*1.8+32
        print("C2F : ",temper,"=>",rt)
    elif action==1:
        ra=(temper-32)/1.8
        print("F2C : ",temper,"=>",ra)
fc(t,a)

#11번 문제

def pzn(num):
    if num>0:
        return 1
    elif num==0:
        return 0
    elif num<0:
        return -1
while True:
    n=int(input("정수 : "))
    if pzn(n)==1:
        print("양수")
    elif pzn(n)==-1:
        print("음수")
    elif pzn(n)==0:
        print("0")
        break

#12번 문제

def vsum(*num): # *num : 튜플형, 복수의 인수 입력가능
    s=0
    for i in num:
        s+=i       
    return s

print(vsum(2,3))
print(vsum(2,3,4))
print(vsum(2,3,4,5))
