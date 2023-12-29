N = int(input())
C = sorted(list(map(int, input().split())))

target = 1
for c in C:
    if target < c:
        break
    
    target += c

print(target)