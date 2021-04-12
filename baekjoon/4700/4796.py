"""
문제 링크: https://www.acmicpc.net/problem/4796
문제 접근 방법: 브루트포스
"""

i = 1
while True:
    L, P, V = map(int,input().split())
    
    if L ==0 and P ==0 and V ==0:
        break
    
    res = int(V / P) * L
    res += min(V%P, L)

    print("Case " + str(i) +": " + str(res))

    i+=1