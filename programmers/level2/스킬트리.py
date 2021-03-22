"""
문제 링크: https://programmers.co.kr/learn/courses/30/lessons/49993
문제 접근 방법: 단순 구현, skill에 있는 문자열을 제외한 모든 문자열을 제거하고 skill의 순서대로 skill_tree들이 잘 구성됐는지 하나하나 검사했다. 간단한 구현이긴한데, 코드를 간결하게 작성못한 부분이 조금 아쉬웠다.
"""

def solution(skill, skill_trees):
    alphabet_list = []
    for i in range(65, 91):
        alphabet_list.append(skill.count(chr(i)))
    
    for i in range(len(skill_trees)):
        new_skill = ""
        for j in skill_trees[i]:
            if alphabet_list[ord(j)-65] == 1:
                new_skill += j
        skill_trees[i] = new_skill
    
    answer = 0
    
    for i in range(len(skill_trees)):
        if len(skill_trees[i]) == 0:
            answer+=1
        else:
            k = 0
            answer+=1
            for j in skill_trees[i]:
                if j == skill[k]:
                    k+=1
                else:
                    answer-=1
                    break
        
    return answer