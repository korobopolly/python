#리스트와 튜플 사용하기 (1)

#1.리스트 만들기
'''
a=[38,21,53,62,19]
print(a)

b=[]
print(b)

c=list()
print(c)

d=["Hello",10,3.5,True,False,[1,2],a]
print(d)
'''
#2.list(),range() 함수 사용하기
'''
a=list(range(10))
print(a)

b=list([1,2,3,4,5])
print(b)

c=list(range(1,6))
print(c)

d=list(range(10,20,2))
print(d)

print(list("Hello"))
'''
#3.리스트 요소에 접근하기
'''
a=[38,21,53,62,19]
print(a)
print(a[0])
print(a[1])
print(a[3])
print(a[-1])
print(a[-3])
#print(a[5]) 리스트의 범위를 벗어나 접근하면 에러!
'''
#4.리스트 요소에 값 할당하기
'''
b=[0,0,0,0,0]
b[0]=38
b[1]=21
b[2]=53
b[3]=62
b[4]=19
print (b)
'''
#5.리스트의 길이(요소의 개수)
'''
a=[1,2,3,4,5,6,7,8,9,10]
print(len(a))
b=list(range(1234,5678,7))
print(len(b))
'''
#6.리스트의 구간 접근
'''
b=[38,21,53,62,19]
print(b[0:3])
print(b[3:6])
print(b[3:3])

print(b[:3])
print(b[3:])
print(b[:])
'''
#7.튜플 사용하기
#리스트, 튜플 - 순서 상관있음. 집합 - 순서 상관 없음.
a=(38,21,53,62,19)
print(a)
b=1,2,3,4,5 #튜플은 괄호 생략 가능
print(b)

print(a[0]) #a[0]=10 튜플은 리스트와 다르게 요소 값을 변경 불가
print(b[3])

print(len(a))

print((38)) #값 38
print((38,)) #요소가 하나인 튜플을 만들려면 값 하나에 반드시 ,를 붙여준다.

c=1,2,3,4,5
print(c)
print(list(c)) #튜플을 리스트로 변환
d=list(c)
print(tuple(d)) #리스트를 튜플로 변환
#리스트에 튜플 요소가 포함되거나 튜플에 리스트 요소가 포함될 수 있다.
