def solution(N, floors, k):
    answer=0
    j=0
    for i in floors:
        if abs(i-j)>=k:
            answer += abs(i-j)
        j = i
    return answer

N=10
floors = [1, 3, 9, 7, 4, 2, 5, 6, 10, 8]
k=3
ret=solution(N, floors, k)
print(ret)
