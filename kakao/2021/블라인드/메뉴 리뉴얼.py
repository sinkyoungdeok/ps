"""
문제 링크: https://programmers.co.kr/learn/courses/30/lessons/72411
문제 접근 방법: 구현
"""
from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for c in course:
        combi_list = []
        for order in orders:
            combi = combinations(sorted(order), c)
            for cb in combi:
                combi_list.append(cb)
        counter = Counter(combi_list)
        if len(counter) >= 1 and max(counter.values()) > 1:
            for ct in counter:
                if counter[ct] == max(counter.values()):
                    answer.append(''.join(ct))
    return sorted(answer)

orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2,3,5]
print(solution(orders,course))