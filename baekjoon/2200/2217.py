"""
문제 링크: https://www.acmicpc.net/problem/2217
문제 접근 방법: 브루트포스, 큰수로 정렬 후에 각 값 * 순회횟수로 제일 큰값을 찾아내는 방식으로 해결 했다.
"""

N = int(input())

w = []
for _ in range(N):
    w.append(int(input()))

w.sort(reverse=True)

res = 0
for i in range(N):
    if res < (i+1) * w[i]:
        res = (i+1) * w[i]

print(res)
