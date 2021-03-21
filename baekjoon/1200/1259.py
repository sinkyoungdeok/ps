"""
문제 링크: https://www.acmicpc.net/problem/1259
문제 접근 방법: 입력받은 값 == 뒤짚은 값 
"""

while True:
    N = int(input())
    if N == 0:
        break
    
    if str(N) == str(N)[::-1]:
        print("yes")
    else:
        print("no")
