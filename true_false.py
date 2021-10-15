'''
kor_score=int(input("국어 점수 : "))
eng_score=int(input("영어 점수 : "))

if kor_score < 80 or eng_score < 80:
    print("불합격입니다.")
else:
    print("합격입니다.")


num=int(input("양의 정수 : "))
if num%2==0:
    print("짝수")
elif num%2==1:
    print("홀수")
else:
    print("오류")


num=int(input("정수 : "))
if num==0:
    print("0")
elif num>0:
    print("양수")
else:
    print("음수")
'''

score = int(input("점수 : "))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
