def func_a(card1, card2):
    return int(card1+card2)
def solution(card1, card2):
    num1 = func_a(card1, card2)
    num2 = func_a(card2, card1)
    return min(num1, num2)

card1="350"
card2="2"
ret = solution(card1, card2)
print(ret)
