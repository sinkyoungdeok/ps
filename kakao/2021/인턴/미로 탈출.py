import heapq

def solution(n, start, end, roads, traps):
    adj = [[] for _ in range(n+1)]
    trap_dict = {trap : i for i, trap in enumerate(traps)}
    traps = set(traps)
    
    for P, Q, S in roads:
        adj[P].append((Q, S))
        adj[Q].append((P, -S))
    
    pq = [ (0, start, 0)]
    dist = {}
    
    while pq:
        cost, curr, state = heapq.heappop(pq)
        
        if dist.get((curr, state)):
            continue
        dist[(curr,state)] = cost
        
        if curr == end: 
            return cost
        
        direction = 1
        
        if curr in traps and (state & (1 << trap_dict[curr])):
            direction *= -1
        
        for next, c in adj[curr]:
            if next in traps and (state & (1 << trap_dict[next])):
                c *= -1 
            if c * direction <= 0:
                continue
                

            if next in traps:
                if state & (1 << trap_dict[next]):
                    new_state = state & ~(1 << trap_dict[next])
                else:
                    new_state = state | (1 << trap_dict[next])
            else:
                new_state = state
                
            heapq.heappush(pq, (cost + abs(c), next, new_state))

    return -1