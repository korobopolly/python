s1=0
s2=0
for i in range(1,51,1):
    if i%2==1:
        s1+=i
    elif i%2==0:
        s2+=i
print ("1부터 50까지의 짝수의 합 : ",s2)
print ("1부터 50까지의 홀수의 합 : ",s1)
