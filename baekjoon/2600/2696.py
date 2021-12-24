from sys import stdin
import heapq

T = int(stdin.readline())

def play(num_list):

    left, right = [], []
    mid = num_list[0]
    res = [mid]
    for i,v in enumerate(num_list[1:], 1):
        if v > mid:
            heapq.heappush(right, v)
        else:
            heapq.heappush(left, -v)
        if i % 2 == 1:
            continue
        
        if len(left) < len(right):
            heapq.heappush(left, -mid)
            mid = heapq.heappop(right)
        elif len(left) > len(right):
            heapq.heappush(right, mid)
            mid = -heapq.heappop(left)
        res.append(mid)
    
    print(len(res))

    for i in range(len(res)):
        if i != 0 and i % 10 == 0:
            print()
        print(res[i], end= ' ')
    print()

    return 

for _ in range(T):
    M = int(input())
    num_list = []
    
    if M % 10 == 0:
        for _ in range(M // 10):
            num_list.extend(list(map(int, stdin.readline().split())))
    else:
        for _ in range(M // 10 + 1):
            num_list.extend(list(map(int, stdin.readline().split())))

    play(num_list)