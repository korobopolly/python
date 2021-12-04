def func_a(k):
    sum=0
    for i in range(k+1):
        sum+=i
    return sum

def solution(n, m):
    sum_to_m=func_a(m)
    sum_to_n=func_a(n-1)
    answer=sum_to_m-sum_to_n
    return answer

n1=5
m1=10
answer1=solution(n1, m1)
print("solution(n1, m1)의 리턴값: {}".format(answer1))

n2=6
m2=6
answer2=solution(n2, m2)
print("solution(n1, m1)의 리턴값: {}".format(answer2))
