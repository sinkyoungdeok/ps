"""
문제 링크: https://programmers.co.kr/learn/courses/30/lessons/64063
문제 접근 방법: 
"""
import sys
sys.setrecursionlimit(10 ** 7)

def find(room, room_dic):
    if room not in room_dic:
        room_dic[room] = room+1
        return room
    room_dic[room] = find(room_dic[room], room_dic)
    return room_dic[room]

def solution(k, room_number):
    answer = []
    room_dic = dict()
    for r in room_number:
        res = find(r, room_dic)
        answer.append(res)
    return answer

k = 10
room_number = [1,3,4,1,3,1]
print(solution(k, room_number))