def solution(price, discount, min_price, money):
    answer=0
    purchase_price = price
    while purchase_price * (answer+1) <= money:
        if purchase_price-discount < min_price:
            purchase_price = min_price
        else:
            purchase_price -= discount
        answer += 1
    return answer

price=30
discount = 3
min_price=17
money =100
ret = solution(price, discount, min_price, money)
print(ret)
