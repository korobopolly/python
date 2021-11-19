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
