"""
문제 링크: https://programmers.co.kr/learn/courses/30/lessons/72411
문제 접근 방법: 구현
"""
from itertools import combinations

def solution(orders, course):
    answer = []
    alphabet_set = set()
    for order in orders:
        for o in order:
            alphabet_set.add(o)
    alphabet_set = list(alphabet_set)
    alphabet_set.sort()
    c_list = []
    for c in course:
        combi = combinations(alphabet_set, c)
        c_temp = []
        for com in combi:
            c_temp.append(''.join(com))
        c_list.append(c_temp)
    res = []

    return answer

orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2,3,5]
print(solution(orders,course))