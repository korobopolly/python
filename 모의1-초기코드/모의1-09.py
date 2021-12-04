def solution(price, money):
    answer=0
    price_sum=0
    for i in price:
        price_sum+=i
        answer=money-price_sum
        if price_sum>money:
            answer=-1
    return answer

price=[2100, 3200, 2100, 800]
money=10000
answer=solution(price, money)
print("solution(price, money)의 리턴값: {}".format(answer))
