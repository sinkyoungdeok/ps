"""
문제 링크: https://programmers.co.kr/learn/courses/30/lessons/67256?language=python3
문제 접근: 방법: 구현
"""

def solution(numbers, hand):
    answer = ''
    key_pad = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9'],
        ['*', '0', '#']
    ]
    key_hash = [
        (3,1),
        (0,0),
        (0,1),
        (0,2),
        (1,0),
        (1,1),
        (1,2),
        (2,0),
        (2,1),
        (2,2),
        (3,0),
        (3,2)
    ]
    
    left_hand = (3,0)
    right_hand = (3,2)
    
    for number in numbers:
        if number == 1 or number == 4 or number == 7:
            answer += 'L'
            left_hand = key_hash[number]
        elif number == 3 or number == 6 or number == 9:
            answer += 'R'
            right_hand = key_hash[number]
        else:
            curr_key = key_hash[number]
            left_dist = abs(curr_key[0]-left_hand[0]) + abs(curr_key[1] - left_hand[1])
            right_dist = abs(curr_key[0]-right_hand[0]) + abs(curr_key[1] - right_hand[1])
            
            if left_dist > right_dist:
                answer += 'R'
                right_hand = curr_key
            elif left_dist < right_dist:
                answer += 'L'
                left_hand = key_hash[number]
            else:
                if hand == "right":
                    answer += 'R'
                    right_hand = curr_key
                else:
                    answer += 'L'
                    left_hand = key_hash[number]
            


    return answer