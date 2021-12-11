def solution(number):
    answer = 0
    while number // 10 !=0:
        temp = 1
        while number != 0:
            temp *=(number % 10)
            number //=10
        number = temp
        answer += 1
    return answer

number1=47
ret1 = solution(number1)
print(ret1)

number2=56
ret2 = solution(number2)
print(ret2)
