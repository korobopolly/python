def solution(answer, choices):
    score = 0
    for choice in choices:
        is_exist = False
        for a in answer:
            if choice == a:
                is_exist = True
        if is_exist:
            score += 1
        else:
            score -= 1
    if score < 0:
        score=0
    return score 

answer1 = [1, 3]
choices1 = [1, 2, 4]
ret1 = solution(answer1, choices1)
print(ret1)

answer2 = [2, 3, 4]
choices2 = [2, 3]
ret2 = solution(answer2, choices2)
print(ret2)
