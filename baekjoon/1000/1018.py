"""
문제 링크: https://www.acmicpc.net/problem/1018
문제 접근 방법: 브루트 포스
"""

n, m = map(int, input().split())
m_list = []
for _ in range(n):
    m_list.append(input())
min_ = 64

for i in range(n - 7):
    for j in range(m - 7):
        count1 = 0
        count2 = 0
        for k in range(i, i + 8):
            for s in range(j, j + 8):
                if k % 2 == 0 and s % 2 == 0:
                    if m_list[k][s] == 'B':
                        count1 += 1
                elif k % 2 == 1 and s % 2 == 1:
                    if m_list[k][s] == 'B':
                        count1 += 1
                elif k % 2 == 0 and s % 2 == 1:
                    if m_list[k][s] == 'W':
                        count1 += 1
                elif k % 2 == 1 and s % 2 == 0:
                    if m_list[k][s] == 'W':
                        count1 += 1
        for k in range(i, i + 8):
            for s in range(j, j + 8):
                if k % 2 == 0 and s % 2 == 0:
                    if m_list[k][s] == 'W':
                        count2 += 1
                elif k % 2 == 1 and s % 2 == 1:
                    if m_list[k][s] == 'W':
                        count2 += 1
                elif k % 2 == 0 and s % 2 == 1:
                    if m_list[k][s] == 'B':
                        count2 += 1
                elif k % 2 == 1 and s % 2 == 0:
                    if m_list[k][s] == 'B':
                        count2 += 1
        min_ = min(min_, count1, count2)
print(min_)