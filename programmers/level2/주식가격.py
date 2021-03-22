"""
문제 링크: https://programmers.co.kr/learn/courses/30/lessons/42584
문제 접근 방법: 단순 구현
"""

def solution(prices):
    answer = []
    for i in range(0,len(prices)):
        cnt = 0
        for j in range(i+1,len(prices)):
            if prices[i] <= prices[j]:
                cnt +=1
            else:
                cnt +=1
                break
        answer.append(cnt)
    return answer