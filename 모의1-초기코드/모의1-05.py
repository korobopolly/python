def solution(stones):
    cnt=0
    current=0
    n=len(stones)
    while current<n:
        current+=stones[current]
        cnt+=1
    return cnt

stones=[2, 5, 1, 3, 2, 1]
answer=solution(stones)
print("solution(stones)의 리턴값: {}".format(answer))
