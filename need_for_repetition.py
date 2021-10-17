'''
import turtle as t
t.shape("turtle")

for i in range(1):
    for i in range(4):
        t.right(90)
        t.forward(100)
        
    for i in range(4):
        t.left(90)
        t.forward(100)

    for i in range(4):
        t.forward(100)
        t.right(90)
        
    for i in range(4):
        t.forward(100)
        t.left(90)

list1=[1,2,3,4,5]
list2=[5,7,9]
list3=[4,6,8]
for a in list2:
    print("파이썬",i)

for a in list3:
    print(a,"학년")
'''

s=0
for i in [1,2,3,4,5]:
    s+=i
print("s :",s)

a=0
list1=[5,4,3,2,1]
for i in list1:
    a+=i
print("a :",a)
