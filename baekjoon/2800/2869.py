"""
문제 링크: https://www.acmicpc.net/problem/2869
문제 접근 방법: 수학
"""

A, B, V = map(int,input().split())

if (V-A)%(A-B) == 0:
    print(int((V-A)/(A-B))+1)
else:
    print(int((V-A)/(A-B))+2)