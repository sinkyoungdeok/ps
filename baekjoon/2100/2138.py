N = int(input())

now = [ int(i) for i in list(input())]
target = [ int(i) for i in list(input())]


def play(now, target):
    cnt = 0
    for i in range(1, N):
        if now[i-1] == target[i-1]:
            continue

        cnt+=1 

        now[i-1] ^= 1
        now[i] ^=1
        if i != (N-1):
            now[i+1] ^=1
    
    if now == target:
        return cnt
    else:
        return 1000000000

def on(now, target):
    now[0] ^= 1
    now[1] ^= 1
    return play(now, target) + 1

def off(now, target):
    return play(now, target)

res = 1000000000
res = min(res, on(now[:], target))
res = min(res, off(now[:], target))

if res >= 1000000000:
    res = -1

print(res)

