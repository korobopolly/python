while True:
    z=int(input("정수 : "))
    res=7*z
    if z>0 and z<=9:
        print("7*",z,"=",res)
    elif z>10:
        print("9이하의 정수로 다시 입력하세요")
    elif z<0:
        break
