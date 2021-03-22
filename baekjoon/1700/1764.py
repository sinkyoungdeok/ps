"""
문제 링크: https://www.acmicpc.net/problem/1764
문제 접근 방법: 정렬
"""

N, M = input().split(" ")

N = int(N)
M = int(M)

result_list = {}

N_set = set()
M_set = set()
for i in range(N):
    N_set.add(input())
for i in range(M):
    M_set.add(input())

result = list(N_set & M_set)
print(len(result))
for re in sorted(result):
    print(re)
