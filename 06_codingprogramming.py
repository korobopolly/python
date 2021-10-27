#1번 문제

s=0
list1=[1, 3, 5, 7, 9]
for i in list1:
    s+=i
    print( i, s)

#2번 문제
list2=["국어", "영어", "수학", "과학", "한국사"]
for i in list2:
    print( i, end=" ")

#3번 문제

name=["홍길동", "임꺽정"]
subject=["국어", "영어", "수학"]

for i in name:
    for j in subject:
        print( i, j)

#4번 문제

s=0
for i in range (1,101):
    s+=i
print(s)

#5번 문제

s1=0
s2=0
for i in range(1,101,1):
    if i%2==1:
        s1+=i
    elif i%2==0:
        s2+=i
print ("홀수 합 : ",s1)
print ("짝수 합 : ",s2)

#6번 문제

s=0
for i in range(3,-4,-1):
    s+=i
    print( i, end=" ")
print()
print(s)

#7번 문제

import sys
maxsize=-sys.maxsize-1
minsize=sys.maxsize
list=[8,7,3,2,9,4,1,6,5]
for i in list:
    if i<maxsize:
        if i<minsize:
            minsize=i
        continue
    elif i>maxsize:
        maxsize=i
print(maxsize, minsize)

#8번 문제

for i in range (1,6):
    for j in range (1,5):
        print("*", end="")
    print()

#9번 문제

for i in range(1,6):
    for j in range(i):
        print("*",end="")
    print()

#10번 문제

for i in range(1,6):
    for j in range(1,6-i):
        print(" ",end="")
    for k in range(i):
        print("*",end="")
    print()

#11번 문제

for i in range(1,6):
    for j in range(1,6-i):
        print(" ",end="")
    for k in range(i):
        print("*",end="")
    for j in range(i-1):
        print("*",end="")
    print()

#12번 문제

s=0
n=1
while n!=0:
    n=int(input("정수 : "))
    s+=n
print("합 : ", s)

#13번 문제

pw=" "
while pw!="pwpass":
    pw=input("비밀번호 : ")
print("LogIn Pass!!")

#14번 문제  

s=0
while True:
    z=int(input("정수 : "))
    if z>0:
        s+=z
    elif z<0:
        continue
    elif z==0:
        break
print("합 : ", s)

#15번 문제

i=1
j=2
while True:
    print(i, "번 접으면", j, "mm")
    if(j>100000):
        break
    i+=1
    j*=2
