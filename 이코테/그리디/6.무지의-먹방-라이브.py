import heapq

def solution(food_times, k):
    answer = -1
    pq = []
    for i, v in enumerate(food_times):
        heapq.heappush(pq, (v, i+1))

    food_len = len(food_times)
    prev = 0

    while pq:
        temp = (pq[0][0] - prev) * food_len

        if k >= temp:
            k -= temp
            prev, _ = heapq.heappop(pq)
            food_len -= 1
        else:
            answer = sorted(pq, key = lambda x: x[1])[k % food_len][1]
            break

    return answer 