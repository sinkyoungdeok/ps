"""
문제 링크: https://www.acmicpc.net/problem/1181
문제 접근 방법: 정렬
"""

N = int(input())

word_list = []

for i in range(N):
    word = input()
    word_list.append((word, len(word))

word_list = list(set(word_list))

word_list.sort(key = lambda word: (word[1], word[0]))

for word in word_list:
    print(word[0], word[1])
