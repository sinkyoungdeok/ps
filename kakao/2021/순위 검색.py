"""
문제 링크: https://programmers.co.kr/learn/courses/30/lessons/72412
문제 접근 방법: 구현
"""
def make_combi(info_list, index, dic_res, dic, sum):
    if index == 4:
        if dic_res.get(sum):
            dic_res[sum].append(int(info_list[4]) * -1)
        else:
            dic_res[sum] = [int(info_list[4]) * -1]
        return

    key1 = dic[info_list[index]]
    key2 = dic["-"]

    make_combi(info_list, index+1, dic_res, dic, sum+key1)
    make_combi(info_list, index+1, dic_res, dic, sum+key2)

def upper_bound(s,e,d,L):
    while (e-s >0):
        m = (s+e)//2
        if(L[m] <= d):
            s = m+1
        else:
            e = m
    return e+1

def solution(info, query):
    answer = []

    dic = {}
    dic["cpp"] = "1"
    dic["java"] = "2"
    dic["python"] = "3"

    dic["backend"] = "1"
    dic["frontend"] = "2"

    dic["junior"] = "1"
    dic["senior"] = "2"

    dic["chicken"] = "1"
    dic["pizza"] = "2"

    dic["-"] = "0"

    dic_res = {}
    for i in info:
        make_combi(i.split(), 0, dic_res, dic, "")

    for key,_ in dic_res.items():
        dic_res[key].sort()
    for q in query:
        key = ""
        q_list = q.split(" ")
        value = -1 * int(q_list[-1])

        for i in range(0,7,2):
            key += dic[q_list[i]]
        if dic_res.get(key):
            answer.append(upper_bound(0,len(dic_res[key]),value, dic_res[key] ) -1)
        else:
            answer.append(0)



    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info,query))