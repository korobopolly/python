def solution(ages):
    answer = 0
    for age in ages:
        if 7>= age or age >=65:
            answer += 1
    return answer
ages = [17, 40, 92, 15, 26, 28, 50, 5]
ret = solution(ages)
print(ret)
