def solution(hint, passwords):
    answer = 0
    for password in passwords:
        is_possible = True
        for i, h in enumerate(hint):
            if h != password[i] and h != "." :
                is_possible = False
        if is_possible == True :
            answer += 1
    return answer

hint1 = "b.d"
passwords1 = ["bad","dad", "bed"]
ret1 = solution(hint1, passwords1)
print(ret1)

hint2 = "...."
passwords2 = ["hand","nose","foot"]
ret2 = solution(hint2, passwords2)
print(ret2)

