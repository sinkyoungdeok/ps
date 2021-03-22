"""
문제 링크: https://www.acmicpc.net/problem/1544
문제 접근 방법: 단어 자체를 정렬해서 중복 제거 
"""

N = int(input())

word_list = {}
for i in range(N):
    word = input()
    
    is_exist = False
    for j in range(len(word)):
        word = word[1:] + word[0]
        if word_list.get(word):
            is_exist = True
    if is_exist == False:
        word_list[word] = True

print(len(word_list))
    
        
