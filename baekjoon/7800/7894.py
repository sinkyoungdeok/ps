import math

T = int(input())

for _ in range(T):
    m = int(input())
    ans = 0
    for i in range(1, m+1):
        ans += math.log10(i)
    print(int(ans+1))