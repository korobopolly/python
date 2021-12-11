def solution(cards):
    answer=True
    a=0
    b=0

    for i in range(len(cards)):
        if i%2==0:
            a += cards[i]
        else:
            b += cards[i]
    
    if a<b:
        answer=False
    return answer

cards1 = [3, 4, 10, 33]
ret1 = solution(cards1)
print(ret1)

cards2 = [10, 3]
ret2 = solution(cards2)
print(ret2)
