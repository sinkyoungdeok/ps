"""
문제 링크: https://www.acmicpc.net/problem/1357
문제 접근 방법: 단순 구현
"""

rev_xy = [int(i[::-1]) for i in input().split(" ")]

result = sum(rev_xy)

print( int(str(result)[::-1]))