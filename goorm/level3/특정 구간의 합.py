"""
문제 링크: https://level.goorm.io/exam/43263/%ED%8A%B9%EC%A0%95-%EA%B5%AC%EA%B0%84%EC%9D%98-%ED%95%A9/quiz/1
문제 접근 방법: 정렬
"""

N = int(input())
n_list = [0] + list(map(int,input().split()))
A, B = map(int,input().split())
for i in range(1, N+1):
    n_list[i] += n_list[i-1]

print(n_list[B] - n_list[A-1])
