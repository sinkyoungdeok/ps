"""
문제 링크: https://programmers.co.kr/learn/courses/30/lessons/17677
문제 접근 방법: 
"""

def solution(str1, str2):
    str1, str2 = str1.lower(), str2.lower()

    s1_list = []
    s2_list = []
    for i in range(1,len(str1)):
        if 'a'<=str1[i-1] <= 'z' and 'a' <= str1[i] <= 'z':
            temp = str1[i-1] + str1[i]
            if temp in s1_list:
                for j in range(2,1001):
                    if not (temp + str(j) in s1_list):
                        s1_list.append(temp+str(j))
                        break
            else:
                s1_list.append(str1[i-1] + str1[i])

    for i in range(1, len(str2)): 
        if 'a'<=str2[i-1] <= 'z' and 'a' <= str2[i] <= 'z':
            temp = str2[i-1] + str2[i]
            if temp in s2_list:
                for j in range(2,1001):
                    if not (temp + str(j) in s2_list):
                        s2_list.append(temp+str(j))
                        break
            else:
                s2_list.append(str2[i-1] + str2[i])
    s1_set = set(s1_list)
    s2_set = set(s2_list)
    U_set = s1_set | s2_set
    N_set = s1_set & s2_set
    U_len = len(U_set)
    N_len = len(N_set)
    if U_len == 0 and N_len == 0:
        answer = 1
    else:
        answer = int(N_len/U_len * 65536)
    return answer

str1 = "aa1+aa2"
str2 = "AAAA12"

print(solution(str1,str2))