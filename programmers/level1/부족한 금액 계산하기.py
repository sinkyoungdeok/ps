def solution(price, money, count):
    answer = 0
    original_price = price

    for _ in range(count):
        money -= price
        price += original_price

    if money < 0:
        answer = money * (-1)

    return answer