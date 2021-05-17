"""
문제 링크: https://level.goorm.io/exam/43250/%EB%B0%B0%EC%97%B4-%ED%95%A9%EC%B9%98%EA%B8%B0/quiz/1
문제 접근 방법: 정렬
"""

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
al, bl = map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

for b in B:
	A.append(b)

A.sort()
print(*A,'')