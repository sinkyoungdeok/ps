def solution(nums):
    answer = 0
    length = len(nums) // 2

    for _ in list(set(nums)) :
        if(answer < length):
            answer +=1

    return answer