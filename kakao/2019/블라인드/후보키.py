from itertools import combinations

def solution(relation):
    r = len(relation)
    c = len(relation[0])
    
    combi = []
    for i in range(1, c+1):
        combi.extend(combinations(range(c),i))
        
    res = []
    for com in combi:
        temp = [tuple([j[k] for k in com]) for j in relation]
        
        if len(set(temp)) != r:
            continue
        
        for re in res:
            if set(re).issubset(set(com)):
                break
        else:
            res.append(com)
                
    return len(res)