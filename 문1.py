#문1
z=int(input("정수를 입력하시오:"))
if z%2==0 and z%3==0:
    print("2와 3으로 나누어 떨어집니다.")
elif z%2==0:
    print("2로 나누어 떨어집니다.")
elif z%3==0:
    print("3으로 나누어 떨어집니다.")
else:
    print("2 또는  3으로 나누어 떨어지지않습니다.")
