r=int(input("반지름 : "))
height=int(input("높이 : "))
def bbul_area(radius,height):
    res=1/3*3.14*radius**2*height
    print("반지름: ", radius, "높이 : ", height,"인 원뿔의 부피는 ",res)
bbul_area(r,height)
