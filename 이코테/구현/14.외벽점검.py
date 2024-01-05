from itertools import permutations
def solution(n, weak, dist):
    answer = 10000000
    w_len = len(weak)
    for i in range(w_len):
        weak.append(weak[i] + n)

    for i in range(w_len):
        weak_list = weak[i:i+w_len]
        for dist_list in permutations(dist):
            start = -1
            weak_index = 0
            for di,d in enumerate(dist_list):
                if start < weak_list[weak_index]:
                    start = weak_list[weak_index] + d
                else:
                    start += d
                while weak_index < w_len and start >= weak_list[weak_index]:
                    weak_index+=1
                if weak_index >= w_len:
                    answer = min(answer, di+1)
                    break
    if answer > len(dist):
        return -1

    return answer

n = 200
weak =[0,100]
dist = [1,1]
print(solution(n,weak,dist))