"""
문제 링크: https://programmers.co.kr/learn/courses/30/lessons/42579
문제 접근 방법: 해시
"""

def solution(genres, plays):
    answer = []

    dic = {}
    for i in range(len(genres)):
        if not dic.get(genres[i]):
            dic[genres[i]] = [plays[i],[(plays[i],i)]]
        else:
            temp = dic.get(genres[i])
            temp[0] += plays[i]
            temp[1].append((plays[i],i))
            dic[genres[i]] = temp
    dic_list = []
    for k,v in dic.items():
        dic_list.append((v,k))
    dic_list.sort(reverse=True)

    for i,_ in dic_list:
        temp_list = sorted(i[1], key=lambda x: (-x[0],x[1]))
        for j in range(2):
            if j >= len(temp_list):
                break
            answer.append(temp_list[j][1])


    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres,plays))