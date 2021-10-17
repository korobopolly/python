'''
for i in range(5):
    print(i, end=" ")
print("\n")

for i in [1,2,3]:
    print(i, end="\n")
print()

for i in range(1,4,1):
    print(i, end="\n")
print()

s=0
for i in range(1,6):
    s+=i
print("s : ",s)


s=0
for i in range (1,10,2):
    s+=i
print("s : ",s)

s=0
for i in range (9,0,-2):
    s+=i
print("s : ",s)


i=1
while i <= 5:
    print(i, end=" ")
    i += 1
print()
print(i)
'''

n=1
s=0
while n <=10:
    if n % 2 ==0:
        s+=n
        print("n : ",n,",s : ",s)
    n+=1
print("s : ",s)
