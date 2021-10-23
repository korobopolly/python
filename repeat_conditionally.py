'''
s=0
n=1
while n<=10:
    if n%2==0:
        s=s+n
    n=n+1

print ("s :",s)

#ctrl+c - 무한루프 중지


s=0
n=2
while n<=10:
    s+=n
    n+=2
print ("s :",s)    


s=0
n=9
while n>=1:
    s+=n
    n-=2
print ("s :",s)

for i in [1,2,3,4,5]:
    if i==4:
        break
    if i%2==0:
        continue
    print(i, end=" ")
print("")
print(i)


s=0
for i in range(1,21):
    if i%2==1:
        continue
    s+=i
    print ("i :",i,", s :",s)
    if s>30:
        break
print ("i :",i,", s :",s)
'''

s=0
for i in range(1,21):
    if i%2==0:
        continue
    s+=i
    print("i :",i,",s :",s)
    if s>30:
        break   
print("i :",i,",s :",s)    
        
    
