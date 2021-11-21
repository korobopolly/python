#리스트와 튜플 사용하기(3)

#1. 리스트에서 최소값, 최대값 및 합계 구하기
'''
#1) 최소값
a=[38,21,53,62,19]
min_a=a[0]
for i in a:
    if min_a>i:
        min_a=i
print(min_a)

#2) 최대값
max_a=a[0]
for i in a:
    if max_a < i:
        max_a=i
print(max_a)

#sort - 정렬 함수
a.sort()
print("최소값 : ", a[0], "최대값 : ", a[len(a)-1])

#min, max 함수 사용하기
print(min(a))
print(max(a))

#3) 요소의 합계 구하기
sum_a=0
for i in a:
    sum_a += i
print(sum_a)

#sum 함수 사용하기
print(sum(a))
'''
#2. 리스트 포함문 사용하기
#리스트 Comprehension - 리스트 내부에서 for 문과 if 문 사용가능 ( [ ] == list() )
'''
#1) for 문 포함
a=[i for i in range(10)]
print(a)
b=list(i*2 for i in range(10))
print(b)

#2) for 문과 if문 포함
a=[i for i in range(10) if i%2==0]
print(a)
b=[i*3 for i in range(10) if i%2!=0]
print(b)

#3) for 문을 중복해서 사용
c=[i*j for i in range(2,10) for j in range(1,10)]
print(c)
'''
#3. 리스트에 map 함수 사용하기
'''
a=[1.2,2.5,3.8,4.7]
for i in range(len(a)):
    a[i]=int(a[i])
print(a)

a=[1.2,2.5,3.8,4.7]
a=list(map(int,a))
print(a)

a=[1.2,2.5,3.8,4.7]
a=[map(int,a)] #함수는 함수 안에서 써야한다.
print(a)

a=[1.2,2.5,3.8,4.7]
a=map(int,a)
print(list(a))

b=list(map(float,range(10)))
print(b)

c=input().split()
print(c)

d=map(int,input().split())
print(list(d))
'''
#4. 튜플에서 메서드 사용
#튜플에서는 변경, 삭제 등을 제외한 메서드만 가능하다.
'''
a=(38,21,38,62,19)
#a[0] = 50
print(a.index(62))
print(a.count(38))

a=(1,2,3)
b=(10,20,30)
c=a+b
print(c)
d=c*2 #배수만큼 반복 출력
print(d)

print(30 in d)
print(40 in d)
print(40 not in d)
'''
#5. 튜플 Comprehansion
'''
a=[i for i in range(10)]
print(a)

a=(i for i in range(10))
#print(list(a))
print(tuple(a))

b=tuple(i for i in range(10) if i%2==0)
print(b)
'''
#6. map함수 및 max, min, sum 함수의 사용
'''
c=(1.2,2.5,3.4,4.7)
c=tuple(map(int,c))
print(c)

print(max(c),
min(c),
sum(c),
sum(c)/len(c))
'''
#7. 2차원 리스트의 사용
'''
a=[[1,2],[10,20]] #2*2 리스트
b=[[1,2,3],[10,20,30],[100,200,300]] #3*3 리스트

print(len(a),len(b)) #아래로 쌓이는 세로줄 수
#인덱스 표현 a[세로 인덱스][가로 인덱스]

print(b[2][2])
'''
#8. 2차원 리스트 모든 요소 출력

a=[[10,20],[30,40],[50,60]] #3*2 리스트

for x,y in a:
    print(x,y)

for i in a:
    for j in i:
        print(j,end=" ")
    print()

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=" ")
    print()
