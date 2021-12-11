def func_a(scores):
    return sum(scores)

def func_b(scores):
    return max(scores)

def func_c(scores):
    return min(scores)

def solution(scores):
    answer = 0
    answer = func_a(scores)
    answer -= func_c(scores)
    return answer

scores = [97, 67, 86, 54, 53, 56] 
ret = solution(scores)
print(ret)
