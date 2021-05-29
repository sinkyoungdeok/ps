"""
문제 링크: https://www.acmicpc.net/problem/1874
문제 접근 방법: 스택
"""

n = int(input())
s = []
res = []
count = 1
check = True
for i in range(n):
    num = int(input())
    while count <= num:
        s.append(count)
        res.append('+')
        count += 1
    if s[-1] == num:
        s.pop()
        res.append('-')
    else:
        print('NO')
        check = False

if check:
    for i in res:
        print(i)