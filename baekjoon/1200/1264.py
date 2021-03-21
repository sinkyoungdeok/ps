"""
문제 링크: https://www.acmicpc.net/problem/1264
문제 접근 방법: 전체를 소문자로 변경 후에 셈 
"""

while True:
    N = input().lower()
    if N == "#":
        break
    
    print(N.count('a') + N.count('e') + N.count('i') + N.count('o') + N.count('u'))
    
