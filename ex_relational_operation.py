'''
x=6
y=2
print(x>y)
print(x>=y)
print(x<y)
print(x<=y)
print(x==y)
print(x!=y)

a=x>y
print(a)
print(type(a))
b=x<y
print(b)
print(type(b))
a=1==1.0 #값의 크기가 같은지 비교
print(a)
b=1 is 1.0 #값의 크기가 아닌 객체를 비교 (저장된 메모리 주소 비교)
print(b)

print(id(1))
print(id(1.0))

print(2>1+1)
print(7//3==2)
print((1+2+3)<=6)
print(6%2==0)
'''

k=90
e=85
print(k>=80 and e>=80)
print(k>=80 or e>=80)
print(k>=80 and e<=80)
print(k>=80 or e<=80)

print("---------------------")
print(3>1 and 3<5)
print(3>1 or 3<5)
print(85>=80 and 85<90)
print(80<85<89)
