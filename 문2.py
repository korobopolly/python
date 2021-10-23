#문2
import random
x=random.randint(1,100)
y=random.randint(1,100)

print(x,'-',y,'=',end="")
z=int(input(" "))

if z==x-y:
    print("맞았습니다.")
else:
    print("틀렸습니다.")
