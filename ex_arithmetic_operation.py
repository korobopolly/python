'''
#사칙연산 계산하기
x=int(input("정수1: "))
y=int(input("정수2: "))

print("x+y=",x+y)
print("x-y=",x-y)
print("x*y=",x*y)
print("x/y=",x/y) #0으로 나눌 경우 오류 발생

odd=1+3+5+7+9
even=2+4+6+8+10
diff=even-odd
print(odd,even,diff)


#날짜 시간 모듈
import datetime as d
ddt=d.date.today()
print(ddt)
#d.date.today().year
#print(d.date.today().year)

name=input("이름 : ")
year=int(input("출생년도: "))
age=ddt.year-year+1
print(name+"의 나이는",age,"입니다.")
'''

# / 연산자에 의한 나눗셈 연산은 피연산자가 둘 다 정수라 하더라도 항상
#실수 연산을 하여 결과값이 실수가 됨

#나눗셈(실수) : / 
#나눗셈(정수) : //
#나머지 : %
#몫과 나머지 내부함수 divmod(a,b)

import sys
divmod(5,2)
print(divmod(5,2))
