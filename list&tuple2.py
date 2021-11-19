#리스트와 튜플 사용하기 (2)

#1.리스트를 조작하는 메서드
'''
#1) append : 리스트 맨 뒤에 값을 추가한다.
a=[10,20]
a.append(30)
print(a)

a.append([40,50])
print(a) #중첩 리스트

#2) insert : 특정 인덱스에 값을 추가한다.
a.insert(2,500)
print(a)

a.insert(len(a),60)
print(a)

#3) extend : 리스트의 맨 뒤에 다른 리스트를 연결한다.
b=[10,20]
b.extend([30,40,50])
print(b)

a.extend(b)
print(a)

#4) remove : 리스트에서 값을 찾아 삭제한다. (동일 값이 여러개 있으면 처음 값만 삭제)
c=[2,7,4,5,7,9]
c.remove(7)
print(c)

#5) pop : 리스트의 마지막 값을 반환하고 삭제한다.
print(c.pop())
print(c)

#6) index : 특정 값의 인덱스를 구한다. (동일 값이 여러개 있으면 처음 값만 반환)
print(c.index(5))

#7) count : 특정 값의 개수를 구한다.
print(a.count(30))
print(a.count(50))

#8) reverse : 리스트의 값의 순서를 반대로 뒤집는다.
a.reverse()
print(a)

#9) sort : 리스트의 값을 작은 순서대로 정렬한다.
a.remove([40,50])
a.sort()
print(a)

#10) clear : 리스트의 모든 값을 삭제한다.
a.clear()
print(a)
'''
#2. 메서드를 사용하지 않고 리스트 조작하기
'''
#1) 리스트 맨 뒤에 값 추가하기 .append
a=[1,2,3]
a[len(a):]=[10]
#a[-1:]=[40]
print(a)

#리스트 접근법
# - 인덱스로 접근 : 범위 안에서만 가능, 값으로 접근
a[1]=20
#a[4]=20 #에러
a[2]=[30] #중첩 리스트
print(a)
# - 범위로 접근 : 범위를 벗어나도 가능, 리스트로 접근
#a[4:]=20 #에러
a[3:]=[20]
a[7:]=[20] #엉뚱한 범위도 가능
a[2:]=[3]
a[:]=[1,2,3,10]
print(a)

#2) 리스트 맨 뒤에 리스트 연결하기 .extend
a[len(a):]=[20,30]
print(a)

#3) del 문을 사용하여 특정 인덱스 값 삭제하기 .remove(값) .pop(인덱스) .clear
del a[1]
print(a)
del a[1:3]
print(a)
del a[:]
print(a)
'''
#3. 리스트 할당과 복사
'''
a=[0,0,0,0,0]
b=a #리스트를 다른 변수에 할당하면 리스트가 2개가 되지않고 동일한 하나이다.
print(b)

b[2]=99
print(b)
print(a)
print(a==b)
print(a is b) #object가 같다. (저장 주소값도 같다.)

a.append(88)
print(b)
print(a==b)
print(a is b)

c=b.copy() #요소는 같으나 2개의 다른 리스트를 만들 때 .copy를 사용한다. 
print(c)
print(a==b)
print(c is b)

c[0]=77
print(c)
print(b)
'''
#4. 리스트 연산하기
'''
a=[1,2,3]
b=[10,20,30]
print(a+b)
#print(a-b)
#print(a*b)
#print(a/b)
print(a*3) #리스트 * 정수는 가능 (0이나 음수를 곱하면 빈 리스트가 된다.)
print(a*0)
print(a*-3)
print("A"*-3)
'''
#5. 리스트 출력하기
'''
#1) for 문에 리스트를 직접 기술
a=[38,21,53,62,19]
for i in a:
    print(i,end=" ")
print()

#2) for, range 함수 사용
for i in range(len(a)):
    print("a[",i,"] =",a[i])

#3) 인덱스와 요소 값을 동시에 출력하려면 for문에 enumerate 함수를 사용합니다.
for i, j in enumerate(a): #인덱스와 값을 세어주는 함수
    print(i, ":", j)

print(53 in a)
print(60 in a)
print(70 not in a)

#4) while 문을 사용하여 리스트를 출력하는 방법
i=0
while i < len(a):
    print(a[i])
    i+=1
'''
