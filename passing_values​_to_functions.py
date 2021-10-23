'''
def calc_gugudan(dan):
    for i in range(1,10):
        print(dan, "*", i, "=", dan*i)

d=int(input("단 : "))
calc_gugudan(d)
'''

def avg(a,b):
    s=(a+b)/2
    return s

in1 = int(input("값1 :"))
in2 = int(input("값2 :"))
r=avg(in1,in2)
print("평균 =",r)
