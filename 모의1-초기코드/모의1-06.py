def solution(height, k):
    answer=0
    n=len(height)
    for h in height:
        if h > k:
            answer+=1
    return answer


height=[165, 170, 175, 180, 184]
k=175
answer=solution(height, k)
print("solution(height, k)의 리턴값: {}".format(answer))
