"""
문제 링크: https://www.acmicpc.net/problem/1427
문제 접근 방법: 단순 구현
"""

N = input()

num_list = []
for i in N:
    num_list.append(int(i))
num_list.sort(key=lambda x:-x)

result = ""
for i in num_list:
    result += str(i)

print(result)